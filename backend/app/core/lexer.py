# platter_lexer.py
# Character-by-character lexer for Platter language
import sys

KEYWORDS = {
    # scalars
    "piece", "crumb", "sip", "feast", "flag", "character", "table",

    # arrays
    "pieces[]", "crumbs[]", "sips[]", "feasts[]", "flags[]", "characters[]",

    # program structure
    "open", "close", "prepare", "start", "serve", "of", "none",

    # control flow
    "check", "alt", "instead", "menu", "choice", "usual",
    "pass", "repeat", "order", "next", "stop",

    # I/O
    "bill", "take",

    # literals
    "up", "down",
}


TWO_CHAR_OPS = {"==", "!=", "<=", ">=", "++", "--", "+=", "-=", "*=", "/=", "%="}
SINGLE_CHAR_OPS = {"+", "-", "*", "/", "%", ">", "<", "=", "!"}
SYMBOLS = {"{", "}", "(", ")", ",", ":", "[" , "]"}
ASSIGN_OPS = {"=", "+=", "-=", "*=", "/=", "%=", ".="}

class Token:
    def __init__(self, type_, value, line, col):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col
    def __repr__(self):
        return f"Token({self.type!r}, {self.value!r})"

class LexerError(Exception):
    pass

class Lexer:
    def __init__(self, text):
        self.text = text or ""
        self.pos = 0
        self.length = len(self.text)
        self.line = 1
        self.col = 1
        self.current = self.text[0] if self.length > 0 else None

    # --- low-level helpers ---
    def peek(self, n=1):
        idx = self.pos + n
        return self.text[idx] if idx < self.length else None

    def advance(self):
        if self.current == "\n":
            self.line += 1
            self.col = 0
        self.pos += 1
        self.col += 1
        self.current = self.text[self.pos] if self.pos < self.length else None

    def make_error(self, message):
        raise LexerError(f"{message} at {self.line}:{self.col}")

    # --- skipping whitespace & comments ---
    def skip_whitespace_and_comments(self):
        while self.current is not None:
            if self.current.isspace():
                self.advance()
                continue
            # comments start with # and go to end of line (docs use #)
            if self.current == "#":
                while self.current is not None and self.current != "\n":
                    self.advance()
                continue
            break

    # --- token readers ---
    def read_identifier_or_keyword(self):
        start_col = self.col
        result = []
        while self.current is not None and (self.current.isalnum() or self.current == "_"):
            result.append(self.current)
            self.advance()
        # check for immediate [] (no whitespace) to accept characters[] token
        if self.current == "[" and self.peek(1) == "]":
            # consume the brackets
            result.append("[]")
            self.advance(); self.advance()
        text = "".join(result)
        if text in KEYWORDS:
            return Token("KEYWORD", text, self.line, start_col)
        return Token("IDENTIFIER", text, self.line, start_col)

    def read_number(self):
        """
        Read a numeric literal. Rules (lexer-level):
        - Must start with digit(s).
        - If there's a '.' after digits: treat as decimal only if the next char after '.' is a digit.
          If the '.' is followed by another '.' (terminator) we do NOT consume it here.
        """
        start_col = self.col
        int_part = []
        while self.current is not None and self.current.isdigit():
            int_part.append(self.current)
            self.advance()
        # possible decimal
        if self.current == ".":
            # if next is '.' then this is not a decimal point, leave the '.' for terminator handling
            if self.peek(1) == ".":
                return Token("NUMBER", "".join(int_part), self.line, start_col)
            # if next is digit -> decimal
            if self.peek(1) is not None and self.peek(1).isdigit():
                # consume dot
                int_part.append(".")
                self.advance()
                frac_part = []
                while self.current is not None and self.current.isdigit():
                    frac_part.append(self.current)
                    self.advance()
                if len(frac_part) == 0:
                    self.make_error("Invalid numeric literal (no digits after decimal point)")
                int_part.extend(frac_part)
                return Token("NUMBER", "".join(int_part), self.line, start_col)
            # if next is something else (like whitespace or letter), this is an invalid '5.' form
            self.make_error("Invalid numeric literal (trailing single dot). Did you mean '..' or a decimal with digits after the dot?")
        return Token("NUMBER", "".join(int_part), self.line, start_col)

    def read_string(self):
        """
        Reads double-quoted string. Supports recognized escape sequences \n, \t, \\, \", \'
        """
        quote = self.current
        start_col = self.col
        self.advance()  # skip opening quote
        result = []
        while self.current is not None and self.current != quote:
            if self.current == "\\":
                # escape
                nxt = self.peek(1)
                if nxt is None:
                    self.make_error("Unfinished escape in string")
                # consume backslash
                self.advance()
                esc = self.current
                if esc == "n":
                    result.append("\n")
                elif esc == "t":
                    result.append("\t")
                elif esc == "\\":
                    result.append("\\")
                elif esc == "\"":
                    result.append("\"")
                elif esc == "'":
                    result.append("'")
                else:
                    # unrecognized escape: docs say treat as raw text — we'll keep the backslash + char
                    result.append("\\" + esc)
                self.advance()
            else:
                result.append(self.current)
                self.advance()
        if self.current != quote:
            self.make_error("Unterminated string literal")
        self.advance()  # skip closing quote
        return Token("STRING", "".join(result), self.line, start_col)

    def read_char(self):
        """
        Reads single-quoted character literal. Per docs: must be exactly one character and NOT an escape
        """
        start_col = self.col
        self.advance()  # skip opening single quote
        if self.current is None:
            self.make_error("Unterminated character literal")
        ch = self.current
        # disallow whitespace or backslash escapes in character (docs)
        if ch.isspace() or ch == "\\":
            self.make_error("Invalid character literal (whitespace or escape not allowed)")
        self.advance()
        if self.current != "'":
            self.make_error("Character literal must be single character enclosed in single quotes")
        self.advance()  # skip closing quote
        return Token("CHAR", ch, self.line, start_col)

    # --- main scanner ---
    def get_next_token(self):
        self.skip_whitespace_and_comments()
        if self.current is None:
            return Token("EOF", None, self.line, self.col)

        # Terminator: ..
        if self.current == ".":
            if self.peek(1) == ".":
                start_col = self.col
                self.advance(); self.advance()
                return Token("TERMINATOR", "..", self.line, start_col)
            # stray single dot or Unicode ellipsis are errors
            if ord(self.current) == 0x2026:  # guard for unicode ellipsis (just in case)
                self.make_error("Unicode ellipsis '…' detected — replace with '..'")
            self.make_error("Unexpected single '.' (Platter statement terminator is '..')")

        # identifier / keyword
        if self.current.isalpha() or self.current == "_":
            return self.read_identifier_or_keyword()

        # number
        if self.current.isdigit():
            return self.read_number()

        # string literal (double quotes)
        if self.current == "\"":
            return self.read_string()

        # char literal (single quotes)
        if self.current == "'":
            return self.read_char()

        # two-char operators
        two = (self.current + (self.peek(1) or ""))
        if two in TWO_CHAR_OPS:
            t = Token("OP", two, self.line, self.col)
            self.advance(); self.advance()
            return t

        # single char operators
        if self.current in SINGLE_CHAR_OPS:
            t = Token("OP", self.current, self.line, self.col)
            self.advance()
            return t

        # symbols
        if self.current in SYMBOLS:
            t = Token("SYMBOL", self.current, self.line, self.col)
            self.advance()
            return t

        # colon and semicolon and comma (':' used in menu choices)
        if self.current in {":", ","}:
            t = Token("SYMBOL", self.current, self.line, self.col)
            self.advance()
            return t

        # anything else is unexpected
        self.make_error(f"Unexpected character {repr(self.current)}")
        return None

    def tokenize(self):
        tokens = []
        while True:
            tok = self.get_next_token()
            tokens.append(tok)
            if tok.type == "EOF":
                break
        return tokens
