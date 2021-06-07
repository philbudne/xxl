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

# XXX XXX XXX PLB take \u{XX...} instead of \uXXXX !!!!
# XXX XXX PLB allow any unicode character in identifier?
# XXX XXX PLB allow any unicode character in identifier?
# XXX PLB replace with native code (likely to be sloooower)

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
        return "<Token %s %s l%d %d:%d>" % \
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
                    self.buf = input('}}} ')
                except (EOFError, KeyboardInterrupt):
                    print('')
                    return ''
                if self.buf:
                    self.buf += '\n'
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
                if isalpha(c) or c.isdigit():
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
            q = c;
            s.advance()
            while True:
                c = s.curr()
                if c < ' ':
                    if c == '\n'  or  c == '\r'  or  c == '':
                        v = "Unterminated string."
                    else:
                        v = "Control Character in string."
                    make('string', str_).error(v)

                # Look for the closing quote.

                if c == q:
                    break

                # Look for escapement.

                if c == '\\':
                    c = s.next()
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
                    elif c == 'u': # XXX change to \u{xx....}
                        h = s.next()
                        h += s.next()
                        h += s.next()
                        h += s.next()
                        if len(h) != 4:
                            make('string', str_).error("Unterminated string")
                        try:
                            c = int(h, 16)
                        except ValueError:
                            make('string', str_).error("Unterminated string")
                        c = chr(c)
                        break
                str_ += c
                s.advance()
            yield make('string', str_)
            c = s.next()

        # comment.
        elif c == '/' and s.peek() == '/':
            s.advance()
            while True:
                c = s.curr()
                if c == '' or c in ['\n', '\r']:
                    break
                s.advance()

        # combining
        elif prefix.find(c) >= 0:
            str_ = c
            s.advance()
            while True:
                c = s.curr()
                if c == '' or suffix.find(c) < 0:
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
    tokenizer = tokenize(sys.stdin)
    t = 1
    while t:
        t = next(tokenizer)
        print(t)
