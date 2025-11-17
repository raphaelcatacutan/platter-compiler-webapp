from app.lexer.token import Token
from app.lexer.protocol import LexerProtocol


class LexerIdentifier(LexerProtocol):
    def s248(self):
        print("s248")
        if self.current in self.id_chars: return self.s250()
        return self.s249()
    
    def s249(self):
        print("s249")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s250(self):
        print("s250")
        self.advance()
        if self.current in self.id_chars: return self.s252()
        return self.s253()
    
    def s253(self):
        print("s253")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s252(self):
        print("s252")
        self.advance()
        if self.current in self.id_chars: return self.s254()
        return self.s257()
    
    def s257(self):  # Accepting state for 3 chars
        print("s257")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s254(self):
        print("s254")
        self.advance()
        if self.current in self.id_chars: return self.s256()
        return self.s261()
    
    def s261(self):  # Accepting state for 4 chars
        print("s261")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s256(self):
        print("s256")
        self.advance()
        if self.current in self.id_chars: return self.s258()
        return self.s265()
    
    def s265(self):
        print("s265")
        print(self.get_lexeme())
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s258(self):
        print("s258")
        self.advance()
        if self.current in self.id_chars: return self.s260()
        return self.s269()
    
    def s269(self): 
        print("s269")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s260(self):
        print("s260")
        self.advance()
        if self.current in self.id_chars: return self.s262()
        return self.s273()
    
    def s273(self):  # Accepting state for 7 chars
        print("s273")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s262(self):
        print("s262")
        self.advance()
        if self.current in self.id_chars: return self.s264()
        return self.s277()
    
    def s277(self):  # Accepting state for 8 chars
        print("s277")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s264(self):
        print("s264")
        self.advance()
        if self.current in self.id_chars: return self.s266()
        return self.s281()
    
    def s281(self):  # Accepting state for 9 chars
        print("s281")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s266(self):
        print("s266")
        self.advance()
        if self.current in self.id_chars: return self.s268()
        return self.s285()
    
    def s285(self):  # Accepting state for 10 chars
        print("s285")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s268(self):
        print("s268")
        self.advance()
        if self.current in self.id_chars: return self.s270()
        return self.s289()
    
    def s289(self):  # Accepting state for 11 chars
        print("s289")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s270(self):
        print("s270")
        self.advance()
        if self.current in self.id_chars: return self.s272()
        return self.s293()
    
    def s293(self):  # Accepting state for 12 chars
        print("s293")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s272(self):
        print("s272")
        self.advance()
        if self.current in self.id_chars: return self.s274()
        return self.s297()
    
    def s297(self):  # Accepting state for 13 chars
        print("s297")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s274(self):
        print("s274")
        self.advance()
        if self.current in self.id_chars: return self.s276()
        return self.s278()
    
    def s278(self):  # Accepting state for 14 chars
        print("s278")
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s276(self):
        print("s276")
        self.advance()
        if self.current in self.id_chars: return self.s280()
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s280(self):
        print("s280")
        self.advance()
        if self.current in self.id_chars: return self.s282()
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s282(self):
        print("s282")
        self.advance()
        if self.current in self.id_chars: return self.s284()
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s284(self):
        print("s284")
        self.advance()
        if self.current in self.id_chars: return self.s286()
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s286(self):
        print("s286")
        self.advance()
        if self.current in self.id_chars: return self.s288()
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s288(self):
        print("s288")
        self.advance()
        if self.current in self.id_chars: return self.s290()
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s290(self):
        print("s290")
        self.advance()
        if self.current in self.id_chars: return self.s292()
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s292(self):
        print("s292")
        self.advance()
        if self.current in self.id_chars: return self.s294()
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s294(self):
        print("s294")
        self.advance()
        if self.current in self.id_chars: return self.s296()
        if self.get_lexeme() in self.KEYWORDS: return Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col)
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s296(self):
        print("s296")
        self.advance()
        while self.current is not None and self.current in self.id_chars: self.advance()
        return Token(Token.ExceedsLimit, self.get_lexeme(), self.start_line, self.start_col)
