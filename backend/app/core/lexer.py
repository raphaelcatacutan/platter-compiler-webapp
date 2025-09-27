class Token:
    def __init__(self, type_, value, line, col):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f"Token({self.type}, {self.value}, line={self.line}, col={self.col})"


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.col = 1
        self.current = self.text[self.pos] if self.text else None

    def advance(self):
        if self.current == "\n":
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        self.pos += 1
        self.current = self.text[self.pos] if self.pos < len(self.text) else None

    def read_full_identifier(self, acc, start_col):
        while self.current is not None and self.current.isalnum():
            acc += self.current
            self.advance()
        return Token("IDENTIFIER", acc, self.line, start_col)

    def get_next_token(self):
        while self.current is not None and self.current.isspace():
            self.advance()

        if self.current is None:
            return None

        start_col = self.col

        # -------------------------------------------------------------------
        # p: piece, pass, prepare
        if self.current == "p":
            acc = "p"; self.advance()
            if self.current == "i":  # piece
                acc += "i"; self.advance()
                if self.current == "e":
                    acc += "e"; self.advance()
                    if self.current == "c":
                        acc += "c"; self.advance()
                        if self.current == "e":
                            acc += "e"; self.advance()
                            if self.current is None or not self.current.isalnum():
                                return Token("KEYWORD", acc, self.line, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "a":  # pass
                acc += "a"; self.advance()
                if self.current == "s":
                    acc += "s"; self.advance()
                    if self.current == "s":
                        acc += "s"; self.advance()
                        if self.current is None or not self.current.isalnum():
                            return Token("KEYWORD", acc, self.line, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "r":  # prepare
                acc += "r"; self.advance()
                if self.current == "e":
                    acc += "e"; self.advance()
                    if self.current == "p":
                        acc += "p"; self.advance()
                        if self.current == "a":
                            acc += "a"; self.advance()
                            if self.current == "r":
                                acc += "r"; self.advance()
                                if self.current == "e":
                                    acc += "e"; self.advance()
                                    if self.current is None or not self.current.isalnum():
                                        return Token("KEYWORD", acc, self.line, start_col)
                                    return self.read_full_identifier(acc, start_col)
                                return self.read_full_identifier(acc, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # c: crumb, character, check, choice, close
        if self.current == "c":
            acc = "c"; self.advance()
            if self.current == "r":  # crumb
                acc += "r"; self.advance()
                if self.current == "u":
                    acc += "u"; self.advance()
                    if self.current == "m":
                        acc += "m"; self.advance()
                        if self.current == "b":
                            acc += "b"; self.advance()
                            if self.current is None or not self.current.isalnum():
                                return Token("KEYWORD", acc, self.line, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "h":
                acc += "h"; self.advance()
                if self.current == "a":  # character
                    acc += "a"; self.advance()
                    if self.current == "r":
                        acc += "r"; self.advance()
                        if self.current == "a":
                            acc += "a"; self.advance()
                            if self.current == "c":
                                acc += "c"; self.advance()
                                if self.current == "t":
                                    acc += "t"; self.advance()
                                    if self.current == "e":
                                        acc += "e"; self.advance()
                                        if self.current == "r":
                                            acc += "r"; self.advance()
                                            if self.current is None or not self.current.isalnum():
                                                return Token("KEYWORD", acc, self.line, start_col)
                                            return self.read_full_identifier(acc, start_col)
                                        return self.read_full_identifier(acc, start_col)
                                    return self.read_full_identifier(acc, start_col)
                                return self.read_full_identifier(acc, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                elif self.current == "e":  # check / choice
                    acc += "e"; self.advance()
                    if self.current == "c":  # check
                        acc += "c"; self.advance()
                        if self.current == "k":
                            acc += "k"; self.advance()
                            if self.current is None or not self.current.isalnum():
                                return Token("KEYWORD", acc, self.line, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    elif self.current == "o":  # choice
                        acc += "o"; self.advance()
                        if self.current == "i":
                            acc += "i"; self.advance()
                            if self.current == "c":
                                acc += "c"; self.advance()
                                if self.current == "e":
                                    acc += "e"; self.advance()
                                    if self.current is None or not self.current.isalnum():
                                        return Token("KEYWORD", acc, self.line, start_col)
                                    return self.read_full_identifier(acc, start_col)
                                return self.read_full_identifier(acc, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "l":  # close
                acc += "l"; self.advance()
                if self.current == "o":
                    acc += "o"; self.advance()
                    if self.current == "s":
                        acc += "s"; self.advance()
                        if self.current == "e":
                            acc += "e"; self.advance()
                            if self.current is None or not self.current.isalnum():
                                return Token("KEYWORD", acc, self.line, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # s: sip, serve, start, stop
        if self.current == "s":
            acc = "s"; self.advance()
            if self.current == "i":  # sip
                acc += "i"; self.advance()
                if self.current == "p":
                    acc += "p"; self.advance()
                    if self.current is None or not self.current.isalnum():
                        return Token("KEYWORD", acc, self.line, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "e":  # serve
                acc += "e"; self.advance()
                if self.current == "r":
                    acc += "r"; self.advance()
                    if self.current == "v":
                        acc += "v"; self.advance()
                        if self.current == "e":
                            acc += "e"; self.advance()
                            if self.current is None or not self.current.isalnum():
                                return Token("KEYWORD", acc, self.line, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "t":  # start / stop
                acc += "t"; self.advance()
                if self.current == "a":  # start
                    acc += "a"; self.advance()
                    if self.current == "r":
                        acc += "r"; self.advance()
                        if self.current == "t":
                            acc += "t"; self.advance()
                            if self.current is None or not self.current.isalnum():
                                return Token("KEYWORD", acc, self.line, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                elif self.current == "o":  # stop
                    acc += "o"; self.advance()
                    if self.current == "p":
                        acc += "p"; self.advance()
                        if self.current is None or not self.current.isalnum():
                            return Token("KEYWORD", acc, self.line, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # f: feast, flag
        if self.current == "f":
            acc = "f"; self.advance()
            if self.current == "e":  # feast
                acc += "e"; self.advance()
                if self.current == "a":
                    acc += "a"; self.advance()
                    if self.current == "s":
                        acc += "s"; self.advance()
                        if self.current == "t":
                            acc += "t"; self.advance()
                            if self.current is None or not self.current.isalnum():
                                return Token("KEYWORD", acc, self.line, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "l":  # flag
                acc += "l"; self.advance()
                if self.current == "a":
                    acc += "a"; self.advance()
                    if self.current == "g":
                        acc += "g"; self.advance()
                        if self.current is None or not self.current.isalnum():
                            return Token("KEYWORD", acc, self.line, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # m: menu
        if self.current == "m":
            acc = "m"; self.advance()
            if self.current == "e":
                acc += "e"; self.advance()
                if self.current == "n":
                    acc += "n"; self.advance()
                    if self.current == "u":
                        acc += "u"; self.advance()
                        if self.current is None or not self.current.isalnum():
                            return Token("KEYWORD", acc, self.line, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # a: alt
        if self.current == "a":
            acc = "a"; self.advance()
            if self.current == "l":
                acc += "l"; self.advance()
                if self.current == "t":
                    acc += "t"; self.advance()
                    if self.current is None or not self.current.isalnum():
                        return Token("KEYWORD", acc, self.line, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # u: usual, up
        if self.current == "u":
            acc = "u"; self.advance()
            if self.current == "s":  # usual
                acc += "s"; self.advance()
                if self.current == "u":
                    acc += "u"; self.advance()
                    if self.current == "a":
                        acc += "a"; self.advance()
                        if self.current == "l":
                            acc += "l"; self.advance()
                            if self.current is None or not self.current.isalnum():
                                return Token("KEYWORD", acc, self.line, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "p":  # up
                acc += "p"; self.advance()
                if self.current is None or not self.current.isalnum():
                    return Token("KEYWORD", acc, self.line, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # d: down
        if self.current == "d":
            acc = "d"; self.advance()
            if self.current == "o":
                acc += "o"; self.advance()
                if self.current == "w":
                    acc += "w"; self.advance()
                    if self.current == "n":
                        acc += "n"; self.advance()
                        if self.current is None or not self.current.isalnum():
                            return Token("KEYWORD", acc, self.line, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # b: bill
        if self.current == "b":
            acc = "b"; self.advance()
            if self.current == "i":
                acc += "i"; self.advance()
                if self.current == "l":
                    acc += "l"; self.advance()
                    if self.current == "l":
                        acc += "l"; self.advance()
                        if self.current is None or not self.current.isalnum():
                            return Token("KEYWORD", acc, self.line, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # n: none, next
        if self.current == "n":
            acc = "n"; self.advance()
            if self.current == "o":  # none
                acc += "o"; self.advance()
                if self.current == "n":
                    acc += "n"; self.advance()
                    if self.current == "e":
                        acc += "e"; self.advance()
                        if self.current is None or not self.current.isalnum():
                            return Token("KEYWORD", acc, self.line, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "e":  # next
                acc += "e"; self.advance()
                if self.current == "x":
                    acc += "x"; self.advance()
                    if self.current == "t":
                        acc += "t"; self.advance()
                        if self.current is None or not self.current.isalnum():
                            return Token("KEYWORD", acc, self.line, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # o: open, of, order, instead
        if self.current == "o":
            acc = "o"; self.advance()
            if self.current == "p":  # open
                acc += "p"; self.advance()
                if self.current == "e":
                    acc += "e"; self.advance()
                    if self.current == "n":
                        acc += "n"; self.advance()
                        if self.current is None or not self.current.isalnum():
                            return Token("KEYWORD", acc, self.line, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "f":  # of
                acc += "f"; self.advance()
                if self.current is None or not self.current.isalnum():
                    return Token("KEYWORD", acc, self.line, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "r":  # order
                acc += "r"; self.advance()
                if self.current == "d":
                    acc += "d"; self.advance()
                    if self.current == "e":
                        acc += "e"; self.advance()
                        if self.current == "r":
                            acc += "r"; self.advance()
                            if self.current is None or not self.current.isalnum():
                                return Token("KEYWORD", acc, self.line, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            elif self.current == "n":  # instead
                acc += "n"; self.advance()
                if self.current == "s":
                    acc += "s"; self.advance()
                    if self.current == "t":
                        acc += "t"; self.advance()
                        if self.current == "e":
                            acc += "e"; self.advance()
                            if self.current == "a":
                                acc += "a"; self.advance()
                                if self.current == "d":
                                    acc += "d"; self.advance()
                                    if self.current is None or not self.current.isalnum():
                                        return Token("KEYWORD", acc, self.line, start_col)
                                    return self.read_full_identifier(acc, start_col)
                                return self.read_full_identifier(acc, start_col)
                            return self.read_full_identifier(acc, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # t: take
        if self.current == "t":
            acc = "t"; self.advance()
            if self.current == "a":
                acc += "a"; self.advance()
                if self.current == "k":
                    acc += "k"; self.advance()
                    if self.current == "e":
                        acc += "e"; self.advance()
                        if self.current is None or not self.current.isalnum():
                            return Token("KEYWORD", acc, self.line, start_col)
                        return self.read_full_identifier(acc, start_col)
                    return self.read_full_identifier(acc, start_col)
                return self.read_full_identifier(acc, start_col)
            return self.read_full_identifier(acc, start_col)

        # -------------------------------------------------------------------
        # numbers
        if self.current.isdigit():
            acc = ""
            while self.current is not None and self.current.isdigit():
                acc += self.current
                self.advance()
            return Token("NUMBER", acc, self.line, start_col)

        # -------------------------------------------------------------------
        # identifiers
        if self.current.isalpha():
            return self.read_full_identifier("", start_col)

        # -------------------------------------------------------------------
        # symbols (explicit ladder)
        if self.current == "{":
            self.advance(); return Token("SYMBOL", "{", self.line, start_col)
        if self.current == "}":
            self.advance(); return Token("SYMBOL", "}", self.line, start_col)
        if self.current == "(":
            self.advance(); return Token("SYMBOL", "(", self.line, start_col)
        if self.current == ")":
            self.advance(); return Token("SYMBOL", ")", self.line, start_col)
        if self.current == "[":
            self.advance(); return Token("SYMBOL", "[", self.line, start_col)
        if self.current == "]":
            self.advance(); return Token("SYMBOL", "]", self.line, start_col)
        if self.current == ",":
            self.advance(); return Token("SYMBOL", ",", self.line, start_col)
        if self.current == ":":
            self.advance(); return Token("SYMBOL", ":", self.line, start_col)
        if self.current == ".":
            self.advance(); return Token("SYMBOL", ".", self.line, start_col)

        # -------------------------------------------------------------------
        # unknown
        acc = self.current
        self.advance()
        return Token("UNKNOWN", acc, self.line, start_col)

    def tokenize(self):
        tokens = []
        while True:
            tok = self.get_next_token()
            tokens.append(tok)
            if tok == None:
                break
        return tokens
