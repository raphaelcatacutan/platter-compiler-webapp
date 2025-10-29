class Token:
    def __init__(self, type_, value, line, col):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f"{self.type:<30} | line={self.line:<3} | col={self.col:<3} | {self.value:<25}"


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
    def get_next_token(self):
        while self.current is not None and self.current.isspace():
            self.advance()
        if self.current is None:
            return None
        start_col = self.col
        start_pos = self.pos
        if self.current == "a":
            self.advance()
            if self.current == "l":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("ALT", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "n":
                self.advance()
                if self.current == "d":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("AND", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "p":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "n":
                            self.advance()
                            if self.current == "d":
                                self.advance()
                                if self.current is None or self.current in " \n\t(":
                                    return Token("APPEND", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "b":
            self.advance()
            if self.current == "i":
                self.advance()
                if self.current == "l":
                    self.advance()
                    if self.current == "l":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("BILL", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "c":
            self.advance()
            if self.current == "h":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "r":
                        self.advance()
                        if self.current == "s":
                            self.advance()
                            if self.current is None or self.current in " \n\t[":
                                return Token("CHARS", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "e":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "k":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("CHECK", self.text[start_pos:self.pos], self.line, start_col)
                    elif self.current == "o":
                        self.advance()
                        if self.current == "i":
                            self.advance()
                            if self.current == "c":
                                self.advance()
                                if self.current == "e":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t":
                                        return Token("CHOICE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current == "y":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("COPY", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "u":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("CUT", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "d":
            self.advance()
            if self.current == "o":
                self.advance()
                if self.current == "w":
                    self.advance()
                    if self.current == "n":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[];=!\"":
                            return Token("FLAG_LITERAL", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "f":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "c":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("FACT", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "l":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "g":
                        self.advance()
                        if self.current is None or self.current in " \n\t[":
                            return Token("FLAG", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "i":
            self.advance()
            if self.current == "n":
                self.advance()
                if self.current == "s":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current == "a":
                                self.advance()
                                if self.current == "d":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t{":
                                        return Token("INSTEAD", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "m":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "h":
                            self.advance()
                            if self.current == "e":
                                self.advance()
                                if self.current == "s":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t(":
                                        return Token("MATCHES", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "e":
                self.advance()
                if self.current == "n":
                    self.advance()
                    if self.current == "u":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("MENU", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "n":
            self.advance()
            if self.current == "e":
                self.advance()
                if self.current == "x":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t;":
                            return Token("NEXT", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("NOT", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "o":
            self.advance()
            if self.current == "f":
                self.advance()
                if self.current is None or self.current in " \n\t":
                    return Token("OF", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "r":
                self.advance()
                if self.current is None or self.current in " \n\t(":
                    return Token("OR", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "r":
                self.advance()
                if self.current == "d":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "r":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("ORDER", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "p":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "s":
                    self.advance()
                    if self.current == "s":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("PASS", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "r":
                self.advance()
                if self.current == "e":
                    self.advance()
                    if self.current == "p":
                        self.advance()
                        if self.current == "a":
                            self.advance()
                            if self.current == "r":
                                self.advance()
                                if self.current == "e":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t":
                                        return Token("PREPARE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "i":
                self.advance()
                if self.current == "e":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current is None or self.current in " \n\t[":
                                return Token("PIECE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "w":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("POW", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "r":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "n":
                    self.advance()
                    if self.current == "d":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("RAND", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == "e":
                self.advance()
                if self.current == "m":
                    self.advance()
                    if self.current == "o":
                        self.advance()
                        if self.current == "v":
                            self.advance()
                            if self.current == "e":
                                self.advance()
                                if self.current is None or self.current in" \n\t(":
                                    return Token("REMOVE", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "p":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "a":
                            self.advance()
                            if self.current == "t":
                                self.advance()
                                if self.current is None or self.current in " \n\t(":
                                    return Token("REPEAT", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "v":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "r":
                            self.advance()
                            if self.current == "s":
                                self.advance()
                                if self.current == "e":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t(":
                                        return Token("REVERSE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "s":
                self.advance()
                if self.current == "e":
                    self.advance()
                    if self.current == "a":
                        self.advance()
                        if self.current == "r":
                            self.advance()
                            if self.current == "c":
                                self.advance()
                                if self.current == "h":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t(":
                                        return Token("SEARCH", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "s":
            self.advance()
            if self.current == "e":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "v":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current is None or self.current in " \n\t":
                                return Token("SERVE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "i":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current is None or self.current in " \n\t[":
                        return Token("SIP", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "z":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("SIZE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "q":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("SQRT", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("SORT", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "t":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "r":
                        self.advance()
                        if self.current == "t":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("START", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "t":
                self.advance()
                if self.current == "o":
                    self.advance()
                    if self.current == "p":
                        self.advance()
                        if self.current is None or self.current in " \n\t;":
                            return Token("STOP", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "t":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "b":
                    self.advance()
                    if self.current == "l":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current is None or self.current in " \n\t":
                                return Token("TABLE", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "k":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("TAKE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "c":
                    self.advance()
                    if self.current == "h":
                        self.advance()
                        if self.current == "a":
                            self.advance()
                            if self.current == "r":
                                self.advance()
                                if self.current == "s":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t(":
                                        return Token("TOCHARS", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "p":
                    self.advance()
                    if self.current == "i":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current == "c":
                                self.advance()
                                if self.current == "e":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t(":
                                        return Token("TOPIECE", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "s":
                    self.advance()
                    if self.current == "i":
                        self.advance()
                        if self.current == "p":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("TOSIP", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "u":
            self.advance()
            if self.current == "p":
                self.advance()
                if self.current is None or self.current in " \n\t()[];=!\"":
                    return Token("FLAG_LITERAL", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "s":
                self.advance()
                if self.current == "u":
                    self.advance()
                    if self.current == "a":
                        self.advance()
                        if self.current == "l":
                            self.advance()
                            if self.current is None or self.current in " \n\t:":
                                return Token("USUAL", self.text[start_pos:self.pos], self.line, start_col)
        # ---------------------------------------------------------------
        # PUNCTUATION, OPERATORS, DELIMITERS
        op1_dlm = " \n\tabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789(-_“"
        op2_dlm = " \n\tabcdefghijklmnopqrstuvwxyz(_“"
        equal_dlm = " \n\tabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789([-_“"

        # +
        if self.current == "+":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("+=", "+=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token("+", "+", self.line, self.col)

        # -
        if self.current == "-":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("-=", "-=", self.line, self.col)
            if self.current is None or self.current in op2_dlm:
                return Token("-", "-", self.line, self.col)

        # *
        if self.current == "*":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("*=", "*=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token("*", "*", self.line, self.col)

        # /
        if self.current == "/":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("/=", "/=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token("/", "/", self.line, self.col)

        # %
        if self.current == "%":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("%=", "%=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token("%", "%", self.line, self.col)

        # >
        if self.current == ">":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token(">=", ">=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token(">", ">", self.line, self.col)

        # <
        if self.current == "<":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("<=", "<=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token("<", "<", self.line, self.col)

        # =
        if self.current == "=":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("==", "==", self.line, self.col)
            if self.current is None or self.current in equal_dlm:
                return Token("=", "=", self.line, self.col)

        # !
        if self.current == "!":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("!=", "!=", self.line, self.col)
            return Token("!", "!", self.line, self.col)

        # space
        if self.current == " ":
            self.advance()
            return Token(" ", " ", self.line, self.col)

        # tab
        if self.current == "\t":
            self.advance()
            return Token("\t", "\t", self.line, self.col)

        # newline
        if self.current == "\n":
            self.advance()
            return Token("\n", "\n", self.line, self.col)

        # colon
        if self.current == ":":
            self.advance()
            return Token(":", ":", self.line, self.col)

        # braces
        if self.current == "{":
            self.advance()
            return Token("{", "{", self.line, self.col)

        if self.current == "}":
            self.advance()
            return Token("}", "}", self.line, self.col)

        # parentheses
        if self.current == "(":
            self.advance()
            return Token("(", "(", self.line, self.col)

        if self.current == ")":
            self.advance()
            return Token(")", ")", self.line, self.col)

        # brackets
        if self.current == "[":
            self.advance()
            return Token("[", "[", self.line, self.col)

        if self.current == "]":
            self.advance()
            return Token("]", "]", self.line, self.col)

        # comma
        if self.current == ",":
            self.advance()
            return Token(",", ",", self.line, self.col)

        # ---------------------------------------------------------------
        # IDENTIFIERS
        id_delim = " \n\t()[];=+-*/%!<>,:"

        if self.current is not None and (self.current.isalpha() or self.current == "_"):
            start_col = self.col
            start_pos = self.pos

            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", "", self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)

        # ---------------------------------------------------------------
        # NUMBERS
        num_delim = " \n\t()[];=+-*/%!<>,:"


        if self.current is not None and (self.current.isdigit() or self.current == "-"):
            start_col = self.col
            start_pos = self.pos

            # optional negative sign
            if self.current == "-":
                self.advance()
                if self.current is None or self.current in num_delim:
                    return Token("-", "-", self.line, start_col)

            # digit 1
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 2
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif self.current.isdigit():
                goto_decimal = False
            else:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 3
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 4
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 5
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 6
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 7
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 8
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 9
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 10
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 11
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 12
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 13
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 14
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 15 (last whole number digit)
            if self.current is None or self.current in num_delim:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                self.advance()
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            else:
                goto_decimal = False
            if not goto_decimal:
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)

            # decimal part (7 digits max)
            # digit 1
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 2
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 3
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 4
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 5
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 6
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 7
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # finished parsing valid number
            return Token("NUMBER", self.text[start_pos:self.pos], self.line, start_col)

        # ---------------------------------------------------------------
        # STRING
        if self.current == '"':
            start_col = self.col
            start_pos = self.pos
            self.advance()
            while self.current is not None and self.current != '"':
                if self.current == "\\" and self.pos + 1 < len(self.text):
                    self.advance()
                self.advance()
            if self.current == '"':
                self.advance()
                # capture including quotes
                value = self.text[start_pos:self.pos]
                return Token("CHARS_LITERAL", value, self.line, start_col)
            ch = self.text[start_pos]
            self.advance()
            return Token("UNKNOWN", ch, self.line, start_col)

        # ---------------------------------------------------------------
        # COMMENTS
        if self.current == "#":
            start_col = self.col
            self.advance()
            if self.current == "#":  # multi-line
                self.advance()
                start_pos = self.pos
                while self.current is not None:
                    if self.current == "#" and self.pos + 1 < len(self.text) and self.text[self.pos + 1] == "#":
                        self.advance()
                        self.advance()
                        return Token("COMMENT_MULTI", self.text[start_pos:self.pos - 2], self.line, start_col)
                    self.advance()
                ch = "#"  # unclosed ##
                self.advance()
                return Token("UNKNOWN", ch, self.line, start_col)
            elif self.current == " ":
                self.advance()
                start_pos = self.pos
                while self.current is not None and self.current != "\n":
                    self.advance()
                return Token("COMMENT_SINGLE", self.text[start_pos:self.pos], self.line, start_col)
            ch = "#"
            self.advance()
            return Token("UNKNOWN", ch, self.line, start_col)


        # ---------------------------------------------------------------
        # FALLBACK
        ch = self.current
        start_col = self.col
        self.advance()
        return Token("UNKNOWN", ch, self.line, start_col)
    def tokenize(self):
        tokens = []
        while True:
            tok = self.get_next_token()
            tokens.append(tok)
            if tok is None:
                break
        return tokens
