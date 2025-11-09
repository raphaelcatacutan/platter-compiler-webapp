class Token:
    def __init__(self, type_, value, line, col):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f"{self.type:<20} | line={self.line:<3} | col={self.col:<3} | {self.value:<25}"

    InvalidCharacter = "Invalid Character"
    InvalidLexeme = "Invalid Lexeme"

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

    def save(self):
        return (self.pos, self.col, self.current)

    def restore(self, s):
        self.pos, self.col, self.current = s

    # ----------------------------------------------------------
    def get_next_token(self):
        if self.current is None:
            return None

        start_pos = self.pos
        start_col = self.col

        # ---------- a ----------
        saved = self.save()
        if self.current == "a":
            self.advance()
            if self.current == "l":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("alt", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "n":
                self.advance()
                if self.current == "d":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("and", self.text[start_pos:self.pos], self.line, start_col)
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
                                    return Token("append", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- b ----------
        saved = self.save()
        if self.current == "b":
            self.advance()
            if self.current == "i":
                self.advance()
                if self.current == "l":
                    self.advance()
                    if self.current == "l":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("bill", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- c ----------
        saved = self.save()
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
                                return Token("chars", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "e":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "k":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("check", self.text[start_pos:self.pos], self.line, start_col)
                    elif self.current == "o":
                        self.advance()
                        if self.current == "i":
                            self.advance()
                            if self.current == "c":
                                self.advance()
                                if self.current == "e":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t":
                                        return Token("choice", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current == "y":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("copy", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "u":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("cut", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- d ----------
        saved = self.save()
        if self.current == "d":
            self.advance()
            if self.current == "o":
                self.advance()
                if self.current == "w":
                    self.advance()
                    if self.current == "n":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[];=!\"":
                            return Token("flat_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)
        # ---------- f ----------
        saved = self.save()
        if self.current == "f":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "c":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("fact", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "l":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "g":
                        self.advance()
                        if self.current is None or self.current in " \n\t[":
                            return Token("flag", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- i ----------
        saved = self.save()
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
                                        return Token("instead", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- m ----------
        saved = self.save()
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
                                        return Token("matches", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "e":
                self.advance()
                if self.current == "n":
                    self.advance()
                    if self.current == "u":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("menu", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- n ----------
        saved = self.save()
        if self.current == "n":
            self.advance()
            if self.current == "e":
                self.advance()
                if self.current == "x":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t;":
                            return Token("next", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("not", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)
        # ---------- o ----------
        saved = self.save()
        if self.current == "o":
            self.advance()
            if self.current == "f":
                self.advance()
                if self.current is None or self.current in " \n\t":
                    return Token("of", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "r":
                self.advance()
                if self.current is None or self.current in " \n\t(":
                    return Token("or", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "d":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "r":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("order", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- p ----------
        saved = self.save()
        if self.current == "p":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "s":
                    self.advance()
                    if self.current == "s":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("pass", self.text[start_pos:self.pos], self.line, start_col)
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
                                        return Token("prepare", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "i":
                self.advance()
                if self.current == "e":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current is None or self.current in " \n\t[":
                                return Token("piece", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "w":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("pow", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- r ----------
        saved = self.save()
        if self.current == "r":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "n":
                    self.advance()
                    if self.current == "d":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("rand", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "e":
                self.advance()
                if self.current == "m":
                    self.advance()
                    if self.current == "o":
                        self.advance()
                        if self.current == "v":
                            self.advance()
                            if self.current == "e":
                                self.advance()
                                if self.current is None or self.current in " \n\t(":
                                    return Token("remove", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "p":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "a":
                            self.advance()
                            if self.current == "t":
                                self.advance()
                                if self.current is None or self.current in " \n\t(":
                                    return Token("repeat", self.text[start_pos:self.pos], self.line, start_col)
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
                                        return Token("reverse", self.text[start_pos:self.pos], self.line, start_col)
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
                                        return Token("search", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- s ----------
        saved = self.save()
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
                                return Token("serve", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "i":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current is None or self.current in " \n\t[":
                        return Token("sip", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "z":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("size", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "q":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("sqrt", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("sort", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "t":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "r":
                        self.advance()
                        if self.current == "t":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("start", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "o":
                    self.advance()
                    if self.current == "p":
                        self.advance()
                        if self.current is None or self.current in " \n\t;":
                            return Token("stop", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- t ----------
        saved = self.save()
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
                                return Token("table", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "k":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("take", self.text[start_pos:self.pos], self.line, start_col)
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
                                        return Token("tochars", self.text[start_pos:self.pos], self.line, start_col)
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
                                        return Token("topiece", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "s":
                    self.advance()
                    if self.current == "i":
                        self.advance()
                        if self.current == "p":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("tosip", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- u ----------
        saved = self.save()
        if self.current == "u":
            self.advance()
            if self.current == "p":
                self.advance()
                if self.current is None or self.current in " \n\t()[];=!\"":
                    return Token("flag_lit", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "s":
                self.advance()
                if self.current == "u":
                    self.advance()
                    if self.current == "a":
                        self.advance()
                        if self.current == "l":
                            self.advance()
                            if self.current is None or self.current in " \n\t:":
                                return Token("usual", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # symbols

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
            return Token("space", " ", self.line, self.col)

        # tab
        if self.current == "\t":
            self.advance()
            return Token("tab", "\\t", self.line, self.col)

        # newline
        if self.current == "\n":
            self.advance()
            return Token("newline", "\\n", self.line, self.col)

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

        # semicolon
        if self.current == ";":
            self.advance()
            return Token(";", ";", self.line, self.col)

        # -- Helper Strings --
        # explicitly defined as requested, no .isalpha() or .isdigit()
        ID_START = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
        ID_BODY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789"
        DIGITS = "0123456789"
        num_delim = " \t\n,()];=+-*/%!<>:"
        id_delim = " \t\n()[];=+-*/%!<>,:"

        # =========================
        # 1. IDENTIFIERS (Max 25 chars)
        # =========================
        if self.current is not None and self.current in ID_START:
            start_col = self.col
            start_pos = self.pos
            self.advance()

            # We use a 'ladder' pattern: check if next char is valid.
            # If YES: advance and continue deeper into the nest.
            # If NO (or None): we hit a delimiter, return the token immediately.

            # Char 2
            if self.current is not None and self.current in ID_BODY:
                self.advance()
                # Char 3
                if self.current is not None and self.current in ID_BODY:
                    self.advance()
                    # Char 4
                    if self.current is not None and self.current in ID_BODY:
                        self.advance()
                        # Char 5
                        if self.current is not None and self.current in ID_BODY:
                            self.advance()
                            # Char 6
                            if self.current is not None and self.current in ID_BODY:
                                self.advance()
                                # Char 7
                                if self.current is not None and self.current in ID_BODY:
                                    self.advance()
                                    # Char 8
                                    if self.current is not None and self.current in ID_BODY:
                                        self.advance()
                                        # Char 9
                                        if self.current is not None and self.current in ID_BODY:
                                            self.advance()
                                            # Char 10
                                            if self.current is not None and self.current in ID_BODY:
                                                self.advance()
                                                # Char 11
                                                if self.current is not None and self.current in ID_BODY:
                                                    self.advance()
                                                    # Char 12
                                                    if self.current is not None and self.current in ID_BODY:
                                                        self.advance()
                                                        # Char 13
                                                        if self.current is not None and self.current in ID_BODY:
                                                            self.advance()
                                                            # Char 14
                                                            if self.current is not None and self.current in ID_BODY:
                                                                self.advance()
                                                                # Char 15
                                                                if self.current is not None and self.current in ID_BODY:
                                                                    self.advance()
                                                                    # Char 16
                                                                    if self.current is not None and self.current in ID_BODY:
                                                                        self.advance()
                                                                        # Char 17
                                                                        if self.current is not None and self.current in ID_BODY:
                                                                            self.advance()
                                                                            # Char 18
                                                                            if self.current is not None and self.current in ID_BODY:
                                                                                self.advance()
                                                                                # Char 19
                                                                                if self.current is not None and self.current in ID_BODY:
                                                                                    self.advance()
                                                                                    # Char 20
                                                                                    if self.current is not None and self.current in ID_BODY:
                                                                                        self.advance()
                                                                                        # Char 21
                                                                                        if self.current is not None and self.current in ID_BODY:
                                                                                            self.advance()
                                                                                            # Char 22
                                                                                            if self.current is not None and self.current in ID_BODY:
                                                                                                self.advance()
                                                                                                # Char 23
                                                                                                if self.current is not None and self.current in ID_BODY:
                                                                                                    self.advance()
                                                                                                    # Char 24
                                                                                                    if self.current is not None and self.current in ID_BODY:
                                                                                                        self.advance()


            if self.current in id_delim:
                self.advance()
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            else:
                self.advance()
                return Token("Invalid", self.text[start_pos:self.pos], self.line, start_col)

        # =========================
        # 2. NUMBERS (15 whole + 7 decimal)
        # =========================
        if self.current is not None and (self.current in DIGITS or self.current == "-"):
            start_col = self.col
            start_pos = self.pos
            is_decimal = False
            token_type = "piece_lit"

            # Handle negative sign
            if self.current == "-":
                self.advance()
                # If standard demands it must have a digit after '-', check here:
                if self.current is None or self.current not in DIGITS:
                    return Token("-", "-", self.line, start_col)

            # --- WHOLE NUMBER PART (Max 15) ---
            # Digit 1
            if self.current is not None and self.current in DIGITS:
                self.advance()
                # Digit 2
                if self.current is not None and self.current in DIGITS:
                    self.advance()
                    # Digit 3
                    if self.current is not None and self.current in DIGITS:
                        self.advance()
                        # Digit 4
                        if self.current is not None and self.current in DIGITS:
                            self.advance()
                            # Digit 5
                            if self.current is not None and self.current in DIGITS:
                                self.advance()
                                # Digit 6
                                if self.current is not None and self.current in DIGITS:
                                    self.advance()
                                    # Digit 7
                                    if self.current is not None and self.current in DIGITS:
                                        self.advance()
                                        # Digit 8
                                        if self.current is not None and self.current in DIGITS:
                                            self.advance()
                                            # Digit 9
                                            if self.current is not None and self.current in DIGITS:
                                                self.advance()
                                                # Digit 10
                                                if self.current is not None and self.current in DIGITS:
                                                    self.advance()
                                                    # Digit 11
                                                    if self.current is not None and self.current in DIGITS:
                                                        self.advance()
                                                        # Digit 12
                                                        if self.current is not None and self.current in DIGITS:
                                                            self.advance()
                                                            # Digit 13
                                                            if self.current is not None and self.current in DIGITS:
                                                                self.advance()
                                                                # Digit 14
                                                                if self.current is not None and self.current in DIGITS:
                                                                    self.advance()
                                                                    # Digit 15
                                                                    if self.current is not None and self.current in DIGITS:
                                                                        self.advance()

            # --- DECIMAL PART (Max 7) ---
            # We check for '.' after any of the whole digits above might have finished.
            if self.current == ".":
                is_decimal = True
                self.advance()
                # Dec 1
                if self.current is not None and self.current in DIGITS:
                    self.advance()
                    # Dec 2
                    if self.current is not None and self.current in DIGITS:
                        self.advance()
                        # Dec 3
                        if self.current is not None and self.current in DIGITS:
                            self.advance()
                            # Dec 4
                            if self.current is not None and self.current in DIGITS:
                                self.advance()
                                # Dec 5
                                if self.current is not None and self.current in DIGITS:
                                    self.advance()
                                    # Dec 6
                                    if self.current is not None and self.current in DIGITS:
                                        self.advance()
                                        # Dec 7
                                        if self.current is not None and self.current in DIGITS:
                                            self.advance()

                token_type = "sip_lit" if is_decimal else "piece_lit"

            if self.current in num_delim:
                self.advance()
                return Token(token_type, self.text[start_pos:self.pos], self.line, start_col)
            else:
                self.advance()
                return Token("Invalid", self.text[start_pos:self.pos], self.line, start_col)

        # =========================
        # 3. STRING LITERALS (Unlimited length via recursion)
        # =========================
        if self.current == '"':
            start_col = self.col
            start_pos = self.pos
            self.advance()  # skip opening "

            self._consume_until_quote()

            if self.current == '"':
                self.advance()  # skip closing "
                return Token("chars_lit", self.text[start_pos:self.pos], self.line, start_col)
            return Token("UNKNOWN", self.text[start_pos:self.pos], self.line, start_col)

        # =========================
        # 4. COMMENTS (Unlimited length via recursion)
        # =========================
        if self.current == '#':
            start_col = self.col
            start_pos = self.pos
            self.advance()

            if self.current == '#':  # Multi-line start '##'
                self.advance()
                # Find closing '##'
                if self._consume_until_multiline_end():
                    # We found '##'. The current pos is AFTER the second '#'.
                    # We want the content BETWEEN the '##' markers.
                    # start_pos + 2 skips the first '##'
                    # self.pos - 2 excludes the last '##'
                    return Token("comment_multi", self.text[start_pos + 2: self.pos - 2], self.line, start_col)
                return Token("UNKNOWN", self.text[start_pos:self.pos], self.line, start_col)
            else:  # Single-line start '#'
                self._consume_until_newline()
                return Token("comment_single", self.text[start_pos:self.pos], self.line, start_col)

    def _consume_until_quote(self):
        """Recursively consumes characters until '"' or EOF."""
        if self.current is None or self.current == '"':
            return
        # Handle escape sequence (simple version)
        if self.current == '\\':
            self.advance()  # consume '\'
            if self.current is not None:
                self.advance()  # consume escaped char
            self._consume_until_quote()  # recurse
            return

        self.advance()
        self._consume_until_quote()  # recurse

    def _consume_until_newline(self):
        """Recursively consumes characters until '\n' or EOF."""
        if self.current is None or self.current == '\n':
            return
        self.advance()
        self._consume_until_newline()

    def _consume_until_multiline_end(self):
        """Recursively consumes until '##' is found."""
        if self.current is None:
            return False

        if self.current == '#':
            self.advance()
            if self.current == '#':
                return True
            return self._consume_until_multiline_end()

        self.advance()
        return self._consume_until_multiline_end()
        
    def tokenize(self):
        tokens = []
        while True:
            tok = self.get_next_token()
            if tok is None:
                break
            tokens.append(tok)
        return tokens
