# from:
# http://crockford.com/javascript/tdop/tdop.html
# https://github.com/douglascrockford/TDOP
# Douglas Crockford
# 2021-05-04
# Public Domain

import sys                      # stderr
import readline                 # enable editing in input()

# Produce simple token objects from a string.
# A simple token object contains these members:
#      type: 'name', 'string', 'number', 'operator', 'EOF', 'ERROR'
#      value: string or number value of the token
#      from: index of first character of the token
#      to: index of the last character + 1

# Comment lines start with //

# Operators are by default single characters. Multicharacter
# operators can be made by supplying a string of prefix and
# suffix characters.
# characters. For example,
#      '<>+-&', '=>&:'
# will match any of these:
#      <=  >>  >>>  <>  >=  +: -: &: &&: &&
#
# All non-ASCII unicode code points can be used in combining operators
# and after a letter or _ in an ID

# PLB: I wrote a native XXL version, but it's slooooooow!

PROMPT1 = "}}} "              # "There are no curly braces in Python!"
PROMPT2 = "... "

NHEX_CHARS = { # number of hex chars for numeric escapes
    'x':2,
    'u':4,
    'U':8
}

class LexError(Exception):
    """
    Class for lexer errors
    """

class Token(object):
    def __init__(self, type_, value, lineno, from_, to, msg=None):
        self.type_ = type_
        self.value = value
        self.from_ = from_
        self.lineno = lineno
        self.to = to
        self.msg = msg

    def __repr__(self):
        return "<Token %s %r l%d %d:%d>" % \
            (self.type_, self.value, self.lineno, self.from_, self.to)

class Stream(object):
    def __init__(self, f, interactive):
        self.f = f
        self.interactive = interactive
        self.nextc = None
        self.reset()
        self.line_ = 1
        self.reset_prompt()
        self.orig = self.prev = ''
        self.origline = self.prevline = -1
        self.advance()

    def reset_prompt(self):
        self.prompt = PROMPT1

    def reset(self):
        self.i = 0
        self.buf = ''

    def change_prompt(self):
        self.prompt = PROMPT2
        #print("change", self.prompt)

    def pos(self):
        return self.i

    def line(self):
        return self.line_

    def getc(self):
        """
        lowest level: return next character from file
        """
        while True:
            if self.buf:
                c = self.buf[0]
                self.buf = self.buf[1:]
                return c
            if self.interactive:
                try:
                    self.buf = input(self.prompt) + '\n'
                except (EOFError, KeyboardInterrupt) as e:
                    print('')
                    return ''
            else:
                self.buf = self.f.readline()

            # save current and prev line for pointer
            self.prev = self.orig
            self.prevline = self.origline
            self.orig = self.buf
            self.origline = self.line_

            if not self.buf:
                return ''

    def pointer(self, line, pos):
        """
        output pointer to start of token to stderr
        """
        if line == self.origline:
            lp = self.orig
        elif line == self.prevline:
            lp = self.prev
        else:
            return
        if lp.strip() == '':
            return
        sys.stderr.write(lp)
        point = []
        i = 1
        for ch in lp:
            if i >= pos:
                break
            if ch == '\t':
                point.append('\t')
            else:
                point.append(' ')
            i += 1
        point.append('^')
        point.append('\n')
        sys.stderr.write(''.join(point))
        sys.stderr.flush()      # needed w/ PyPy3 7.3.1

    def advance(self):
        """
        consume current character (self.ch) and reload
        """
        self.i += 1
        if self.nextc is not None:
            self.ch = self.nextc
            self.nextc = None
        else:
            self.ch = self.getc()
        if self.ch == '\n':
            self.line_ += 1
            self.i = 0

    def next(self):
        self.advance()
        return self.curr()

    def curr(self):
        return self.ch

    def peek(self):
        if self.nextc is None:
            self.nextc = self.getc()
        if self.nextc: 
            return self.nextc
        else:
            return ''

def isalpha(c):
    return c.isalpha() or c == '_'

def isunicode(c):
    """
    return True if `c` is a non-ASCII unicode code point
    """
    return c != '' and ord(c) >= 128

class Tokenizer:
    def __init__(self, f, prefix, suffix, interactive=False):
        self.prefix = prefix
        self.suffix = suffix
        self.c = ''             # Current character.
        self.s = Stream(f, interactive)
        self.from_ = self.s.pos() # The index of the start of the token.
        self.line = self.s.line()
        self.q = None           # The quote character.
        self.reset_prompt()
        self.c = self.s.curr()

    def reset_prompt(self):
        self.s.reset_prompt()

    def reset(self):
        self.s.reset()
        self.c = self.s.curr()

    def make(self, type_, value):
        #print('make', type_, value, self.line, self.from_, self.s.pos())
        self.s.change_prompt()
        return Token(type_, value, self.line, self.from_, self.s.pos())

    def make_error(self, value, msg):
        return Token('ERROR', value, self.line, self.from_, self.s.pos(), msg)

    def pointer(self, line, pos):
        self.s.pointer(line, pos)

    def next(self):
        while self.c:
            self.from_ = self.s.pos()
            self.line = self.s.line()

            # Ignore whitespace.
            if self.c.isspace():
                self.c = self.s.next()
            elif isalpha(self.c):
                str_ = self.c
                self.s.advance()
                while True:
                    self.c = self.s.curr()
                    if isalpha(self.c) or self.c.isdigit() or isunicode(self.c):
                        str_ += self.c
                        self.s.advance()
                    else:
                        break
                return self.make('name', str_)
            elif self.c.isdigit():
                # number.
                # A number cannot start with a decimal point.
                # It must start with a digit, possibly '0'.
                str_ = self.c
                self.s.advance()

                self.c = self.s.curr()
                if self.c == 'x':
                    str_ += self.c
                    self.s.advance()
                    while True:
                        self.c = self.s.curr()
                        if self.c not in '01234567879abcdefACCDEF':
                            break
                        self.s.advance()
                        str_ += self.c
                    try:
                        return self.make('number', int(str_, 0))
                    except ValueError:
                        # test case "0x"
                        return self.make_error(str_, "Bad hex number")

                # Look for more digits.
                while True:
                    self.c = self.s.curr()
                    if not self.c.isdigit():
                        break
                    self.s.advance()
                    str_ += self.c

                # Look for a decimal fraction part.
                if self.c == '.':
                    self.s.advance()
                    str_ += self.c
                    while True:
                        self.c = self.s.curr()
                        if not self.c.isdigit():
                            break
                        self.s.advance()
                        str_ += self.c

                # Look for an exponent part.
                if self.c in ['e', 'E']:
                    str_ += self.c
                    self.c = self.s.next()
                    if self.c in ['-', '+']:
                        str_ += self.c
                        self.c = self.s.next()
                    if not self.c.isdigit():
                        # test case: 1.0eQ
                        return self.make_error(self.c, "Bad exponent")
                    while True:
                        str_ += self.c
                        self.c = self.s.next()
                        if not self.c.isdigit():
                            break
                # Make sure the next character is not a letter.
                if isalpha(self.c):
                    str_ += self.c
                    self.s.advance()
                    # test case "123x"
                    return self.make_error(str_, "Bad number")

                # Convert the string value to a number.
                try:
                    return self.make('number', int(str_))
                except ValueError:
                    try:
                        return self.make('number', float(str_))
                    except ValueError:
                        return self.make_error(str_, "Bad number")
            elif self.c in ["'", '"']:
                # string
                str_ = ''
                self.q = self.c
                escapes = (self.q == '"') # 'string' are "raw" (like Un*x shell)
                self.s.advance()
                multiline = False
                looping = True
                self.c = self.s.curr()
                # check for triple (multi line) quoting
                if self.c == self.q: # doubled quote?
                    self.c = self.s.peek()
                    if self.c == self.q: # three times?
                        self.s.advance() # consume third quote
                        multiline = True
                    else:           # just two -- an empty string
                        looping = False
                #print("esc", escapes, "multi", multiline, "looping", looping)
                while looping:
                    self.c = self.s.curr()
                    if not multiline:
                        if self.c < ' ':
                            if self.c == '\n' or self.c == '\r' or self.c == '':
                                v = "Unterminated string."
                            else:
                                v = "Control Character in string."
                            return self.make_error(str_, v)
                        if self.c == self.q:  # end quote?
                            break
                    elif self.c == self.q:    # multi-line: check for end quote
                        self.c = self.s.next()
                        # XXX check for EOF?
                        #print("e2", self.c)
                        if self.c == self.q: # second quote?
                            self.c = self.s.next() # consume second quote
                            # XXX check for EOF?
                            if self.c == self.q: # a third??
                                break
                            else: # just two
                                str_ += self.q
                    # end multi-line end quote check

                    # Look for escapement.
                    if escapes and self.c == '\\':
                        self.c = self.s.next()
                        #print("escaped", self.c)
                        if self.c == '':
                            return self.make_error(str_, "Unterminated string")
                        if self.c == 'b':
                            self.c = '\b'
                        elif self.c == 'f':
                            self.c = '\f'
                        elif self.c == 'n':
                            self.c = '\n'
                        elif self.c == 'r':
                            self.c = '\r'
                        elif self.c == 't':
                            self.c = '\t';
                        elif self.c == 'v':
                            self.c = '\v';
                        elif self.c == '"'  or  self.c == "'" or  self.c == "\\":
                            pass
                        elif self.c in NHEX_CHARS:
                            n = NHEX_CHARS[self.c]
                            h = ''
                            while len(h) < n:
                                self.c = self.s.next()
                                if self.c == '':
                                    return self.make_error(str_,
                                                           "Unterminated string")
                                h += self.c
                            try:
                                self.c = int(h, 16)
                            except ValueError:
                                return self.make_error(str_,
                                                       "Unterminated string")
                            self.c = chr(self.c)
                        # end c in NHEX_CHARS
                    # end escapement
                    #print("appending", self.c)
                    str_ += self.c
                    self.s.advance()
                # end while
                self.c = self.s.next()
                return self.make('string', str_)
            elif self.c == '/' and self.s.peek() == '/': # comment
                self.s.advance()
                while True:
                    self.c = self.s.curr()
                    if self.c == '' or self.c in ['\n', '\r']:
                        break
                    self.s.advance()

            # combining
            elif self.prefix.find(self.c) >= 0 or isunicode(self.c):
                str_ = self.c
                self.s.advance()
                while True:
                    self.c = self.s.curr()
                    if self.c == '' or (self.suffix.find(self.c) < 0 and not isunicode(self.c)):
                        break
                    str_ += self.c
                    self.s.advance()
                return self.make('operator', str_)

            # single-character operator
            else:
                self.s.advance()
                t = self.c
                self.c = self.s.curr()
                return self.make('operator', t)

        # keep returning EOF
        return self.make('EOF', '')

################

if __name__ == "__main__":
    import sys
    prefix = '<>+-&'
    suffix = '=>&:'
    if len(sys.argv) > 1:
        tokenizer = Tokenizer(open(sys.argv[1]), prefix, suffix, False)
    else:
        tokenizer = Tokenizer(sys.stdin, prefix, suffix, True)
    t = 1
    while t:
        t = tokenizer.next()
        print(t)
        if t:
            tokenizer.pointer(t.lineno, t.from_)
            if t.type_ == 'EOF':
                break
