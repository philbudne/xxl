# from:
# http://crockford.com/javascript/tdop/tdop.html
# https://github.com/douglascrockford/TDOP
# Douglas Crockford
# 2021-05-04
# Public Domain

import readline                 # enable editing in input()

# Produce an array of simple token objects from a string.
# A simple token object contains these members:
#      type: 'name', 'string', 'number', 'operator'
#      value: string or number value of the token
#      from: index of first character of the token
#      to: index of the last character + 1

# Comments of the # type are ignored.

# Operators are by default single characters. Multicharacter
# operators can be made by supplying a string of prefix and
# suffix characters.
# characters. For example,
#      '<>+-&', '=>&:'
# will match any of these:
#      <=  >>  >>>  <>  >=  +: -: &: &&: &&

# XXX PLB replace with native code (it's SLOOOOW!)???

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
    def __init__(self, type_, value, lineno, from_, to):
        self.type_ = type_
        self.value = value
        self.from_ = from_
        self.lineno = lineno
        self.to = to

    def error(self, s):
        # XXX need filename!
        raise LexError("%s at %s:%s" % (s, self.lineno, self.from_))

    def __repr__(self):
        return "<Token %s %r l%d %d:%d>" % \
            (self.type_, self.value, self.lineno, self.from_, self.to)

class Stream(object):
    def __init__(self, f):
        self.f = f
        self.i = 0
        self.buf = None
        self.nextc = None
        self.line_ = 1
        self.advance()

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
            if self.f.isatty():
                # XXX change prompt to "... " if not at top (in statement()?)
                try:
                    # "There are no curly braces in Python!"
                    self.buf = input('}}} ') + '\n'
                except (EOFError, KeyboardInterrupt):
                    print('')
                    return ''
            else:
                self.buf = self.f.readline()
            if not self.buf:
                return ''

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
    return ord(c) >= 128

def tokenize(finput, prefix='<>+-&', suffix='=>&:'):
    """
    returns a generator
    """
    c = ''                      # The current character.
    s = Stream(finput)
    from_ = s.pos()             # The index of the start of the token.
    line = s.line()
    n = 0                       # The number value.
    q = None                    # The quote character.
    str_ = ''                   # The string value.

    #prefix = set(prefix)
    #suffix = set(suffix)

    # Begin tokenization.
    # Loop through this text, one character at a time.
    c = s.curr()
    while c:
        from_ = s.pos()
        line = s.line()

        def make(type_, value):
            #print('make', type_, value, line, from_, s.pos())
            return Token(type_, value, line, from_, s.pos())

        # Ignore whitespace.
        if c.isspace():
            c = s.next()
        elif isalpha(c):
            str_ = c
            s.advance()
            while True:
                c = s.curr()
                if isalpha(c) or c.isdigit() or isunicode(c):
                    str_ += c
                    s.advance()
                else:
                    break
            yield make('name', str_)
        elif c.isdigit():
            # number.
            # A number cannot start with a decimal point.
            # It must start with a digit, possibly '0'.
            str_ = c
            s.advance()

            # XXX handle 0xXXX here

            # Look for more digits.
            while True:
                c = s.curr()
                if not c.isdigit():
                    break
                s.advance()
                str_ += c

            # Look for a decimal fraction part.
            if c == '.':
                s.advance()
                str_ += c
                while True:
                    c = s.curr()
                    if not c.isdigit():
                        break
                    s.advance()
                    str_ += c

            # Look for an exponent part.
            if c in ['e', 'E']:
                str_ += c
                c = s.next()
                if c in ['-', '+']:
                    str_ += c
                    c = s.next()
                if not c.isdigit():
                    make('number', str_).error("Bad exponent")
                while True:
                    str_ += c
                    c = s.next()
                    if not c.isdigit():
                        break
            # Make sure the next character is not a letter.
            if isalpha(c):
                str_ += c
                s.advance()
                make('number', str_).error("Bad number")

            # Convert the string value to a number.
            try:
                yield make('number', int(str_))
            except ValueError:
                try:
                    yield make('number', float(str_))
                except ValueError:
                    make('number', str_).error("Bad number")
        elif c in ["'", '"']:
            # string
            str_ = ''
            q = c
            escapes = (q == '"') # 'string' are "raw" (like Un*x shell)
            s.advance()
            multiline = False
            looping = True
            c = s.curr()
            # check for triple (multi line) quoting
            if c == q:          # doubled quote?
                c = s.peek()
                if c == q:      # three times?
                    s.advance() # consume third quote
                    multiline = True
                else:           # just two -- an empty string
                    looping = False
            #print("esc", escapes, "multi", multiline, "looping", looping)
            while looping:
                c = s.curr()
                if not multiline:
                    if c < ' ':
                        if c == '\n'  or  c == '\r'  or  c == '':
                            v = "Unterminated string."
                        else:
                            v = "Control Character in string."
                        make('string', str_).error(v)
                    if c == q:  # end quote?
                        break
                elif c == q:    # multi-line: check for end quote
                    c = s.next()
                    # XXX check for EOF?
                    #print("e2", c)
                    if c == q: # second quote?
                        c = s.next() # consume second quote
                        # XXX check for EOF?
                        if c == q: # a third??
                            break
                        else: # just two
                            str_ += q
                # end multi-line end quote check

                # Look for escapement.
                if escapes and c == '\\':
                    c = s.next()
                    #print("escaped", c)
                    if c == '':
                        make('string', str_).error("Unterminated string")
                    if c == 'b':
                        c = '\b'
                    elif c == 'f':
                        c = '\f'
                    elif c == 'n':
                        c = '\n'
                    elif c == 'r':
                        c = '\r'
                    elif c == 't':
                        c = '\t';
                    elif c == 'v':
                        c = '\v';
                    elif c == '"'  or  c == "'" or  c == "\\":
                        pass
                    elif c in NHEX_CHARS:
                        n = NHEX_CHARS[c]
                        h = ''
                        while len(h) < n:
                            c = s.next()
                            if c == '':
                                make('string', str_).error("Unterminated string2")
                            h += c
                        try:
                            c = int(h, 16)
                        except ValueError:
                            make('string', str_).error("Unterminated string3")
                        c = chr(c)
                    # end c in NHEX_CHARS
                # end escapement
                #print("appending", c)
                str_ += c
                s.advance()
            # end while
            yield make('string', str_)
            c = s.next()
        elif c == '/' and s.peek() == '/': # comment
            s.advance()
            while True:
                c = s.curr()
                if c == '' or c in ['\n', '\r']:
                    break
                s.advance()

        # combining
        elif prefix.find(c) >= 0 or isunicode(c):
            str_ = c
            s.advance()
            while True:
                c = s.curr()
                if c == '' or (suffix.find(c) < 0 and not isunicode(c)):
                    break
                str_ += c
                s.advance()
            yield make('operator', str_)

        # single-character operator
        else:
            s.advance()
            yield make('operator', c)
            c = s.curr()

    # keep returning EOF
    while True:
        yield None

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        tokenizer = tokenize(open(sys.argv[1]))
    else:
        tokenizer = tokenize(sys.stdin)
    t = 1
    while t:
        t = next(tokenizer)
        print(t)
