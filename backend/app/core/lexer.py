class Token:
    def __init__(self, type_, value, line, col):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col
    def __repr__(self):
        return f"{self.type:<10} | line={self.line:<3} | col={self.col:<3} | {self.value:<15})"

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
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "n":
                self.advance()
                if self.current == "d":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
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
                                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                    return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
        if self.current == "b":
            self.advance()
            if self.current == "i":
                self.advance()
                if self.current == "l":
                    self.advance()
                    if self.current == "l":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
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
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                elif self.current == "e":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "k":
                            self.advance()
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    elif self.current == "o":
                        self.advance()
                        if self.current == "i":
                            self.advance()
                            if self.current == "c":
                                self.advance()
                                if self.current == "e":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                                else:
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                            else:
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "o":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current == "y":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "u":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
        if self.current == "d":
            self.advance()
            if self.current == "o":
                self.advance()
                if self.current == "w":
                    self.advance()
                    if self.current == "n":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
        if self.current == "f":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "c":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "l":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "g":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
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
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                                else:
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                            else:
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
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
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                                else:
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                            else:
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "e":
                self.advance()
                if self.current == "n":
                    self.advance()
                    if self.current == "u":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
        if self.current == "n":
            self.advance()
            if self.current == "e":
                self.advance()
                if self.current == "x":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "o":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
        if self.current == "o":
            self.advance()
            if self.current == "f":
                self.advance()
                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                    return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "r":
                self.advance()
                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                    return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "r":
                self.advance()
                if self.current == "d":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "r":
                            self.advance()
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
        if self.current == "p":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "s":
                    self.advance()
                    if self.current == "s":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
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
                                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                                    else:
                                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                                else:
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                            else:
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "i":
                self.advance()
                if self.current == "e":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "o":
                self.advance()
                if self.current == "w":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
        if self.current == "r":
            self.advance()
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
                                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                    return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                            else:
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                elif self.current == "p":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "a":
                            self.advance()
                            if self.current == "t":
                                self.advance()
                                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                    return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                            else:
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
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
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                                else:
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                            else:
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
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
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                                else:
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                            else:
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
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
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "i":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "i":
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "z":
                self.advance()
                if self.current == "e":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "o":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "q":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            elif self.current == "t":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "r":
                        self.advance()
                        if self.current == "t":
                            self.advance()
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                elif self.current == "o":
                    self.advance()
                    if self.current == "p":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
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
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                elif self.current == "k":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
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
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                                else:
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                            else:
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
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
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                                else:
                                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                            else:
                                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                        else:
                            self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                    else:
                        self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
                else:
                    self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
        if self.current == "u":
            self.advance()
            if self.current == "p":
                self.advance()
                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                    return Token("KEYWORD", self.text[start_pos:self.pos], self.line, start_col)
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
            else:
                self.pos = start_pos; self.col = start_col; self.current = self.text[self.pos]
        if self.current == '"':
            s_line = self.line
            s_col = self.col
            self.advance()
            start = self.pos
            while self.current is not None and self.current != '"':
                if self.current == "\\" and self.pos + 1 < len(self.text):
                    self.advance()
                self.advance()
            if self.current == '"':
                val = self.text[start:self.pos]
                self.advance()
                return Token("STRING", val, s_line, s_col)
            return Token("UNTERMINATED_STRING", self.text[start_pos:self.pos], s_line, s_col)
        if self.current == "#":
            s_line = self.line
            s_col = self.col
            self.advance()
            if self.current == "#":
                self.advance()
                self.advance()
                start = self.pos
                while self.current is not None:
                    if self.current == "#" and self.pos + 1 < len(self.text) and self.text[self.pos + 1] == "#":
                        val = self.text[start:self.pos]
                        self.advance()
                        self.advance()
                        return Token("COMMENT", val, s_line, s_col)
                    self.advance()
                return Token("UNTERMINATED_COMMENT", self.text[start:self.pos], s_line, s_col)
            else:
                start = self.pos
                while self.current is not None and self.current != "\n":
                    self.advance()
                return Token("COMMENT", self.text[start:self.pos], s_line, s_col)
        if self.current.isdigit():
            start = self.pos
            has_dot = False
            while self.current is not None and (self.current.isdigit() or (self.current == "." and not has_dot)):
                if self.current == ".":
                    has_dot = True
                self.advance()
            return Token("NUMBER", self.text[start:self.pos], self.line, start_col)
        if self.current.isalpha() or self.current == "_":
            start = self.pos
            while self.current is not None and (self.current.isalnum() or self.current == "_"):
                self.advance()
            return Token("IDENTIFIER", self.text[start:self.pos], self.line, start_col)
        if self.current in "{}()[];=+-*/%!<>,:.":
            ch = self.current
            self.advance()
            if ch in "+-*/%<>=!":
                if self.current == "=":
                    two = ch + "="
                    self.advance()
                    return Token("SYMBOL", two, self.line, start_col)
            return Token("SYMBOL", ch, self.line, start_col)
        ch = self.current
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
