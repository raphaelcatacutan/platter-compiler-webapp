from app.lexer.lexer import Lexer
from app.lexer.token import Token
from app.parser.token_map import TOKEN_MAP


class Parser:

    def __init__(self, tokens):
        # Remove whitespace & comments
        self.tokens = [t for t in tokens if t.type not in ("space", "tab", "newline", "comment")]
        self.pos = 0
        self.current = self.tokens[self.pos] if self.tokens else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current = self.tokens[self.pos]
        else:
            self.current = None

    def match(self, *types):
        return self.current and self.current.type in types

    def expect(self, token_type):
        if not self.match(token_type):
            if self.current:
                raise SyntaxError(
                    f"Syntax Error: Expected '{token_type}' but got '{self.current.type}' "
                    f"(line {self.current.line}, col {self.current.col})"
                )
            else:
                raise SyntaxError(f"Syntax Error: Expected '{token_type}' but got EOF")
        self.advance()

    # parse func
    def parse(self, text):
        return 0

    # ----------------------------------
    # Grammar Rules (NO AST construction)
    # ----------------------------------

    def parse_program(self):
        while self.current:
            self.parse_statement()
        return True  # no errors

    def parse_statement(self):
        if self.match("piece"):
            self.parse_assignment()
        elif self.match("check"):
            self.parse_conditional()
        elif self.match("repeat"):
            self.parse_loop()
        elif self.match("id"):
            self.parse_function_call()
        else:
            t = self.current
            raise SyntaxError(
                f"Unexpected token '{t.type}' at line {t.line}, col {t.col}"
            )

    # piece x = 5;
    def parse_assignment(self):
        self.expect("piece")
        self.expect("id")
        self.expect("=")

        if self.match("piece_lit", "id"):
            self.advance()
        else:
            t = self.current
            raise SyntaxError(
                f"Invalid assignment value '{t.type}' at line {t.line}, col {t.col}"
            )

        self.expect(";")

    # check (condition) { statements }
    def parse_conditional(self):
        self.expect("check")
        self.expect("(")
        self.parse_expression()
        self.expect(")")
        self.expect("{")
        self.parse_block()
        self.expect("}")

    # repeat (condition) { statements }
    def parse_loop(self):
        self.expect("repeat")
        self.expect("(")
        self.parse_expression()
        self.expect(")")
        self.expect("{")
        self.parse_block()
        self.expect("}")

    def parse_function_call(self):
        self.expect("id")
        self.expect("(")
        if not self.match(")"):
            self.parse_expression_list()
        self.expect(")")
        self.expect(";")

    def parse_block(self):
        while self.current and not self.match("}"):
            self.parse_statement()

    # --- expressions like x > 0, x + 1
    def parse_expression(self):
        self.parse_primary()
        while self.match("+", "-", "*", "/", ">", "<", "==", "!="):
            self.advance()
            self.parse_primary()

    def parse_primary(self):
        if self.match("id") or self.match("piece_lit"):
            self.advance()
        elif self.match("("):
            self.advance()
            self.parse_expression()
            self.expect(")")
        else:
            t = self.current
            raise SyntaxError(
                f"Invalid expression: unexpected token '{t.type}' "
                f"at line {t.line}, col {t.col}"
            )

    def parse_expression_list(self):
        self.parse_expression()
        while self.match(","):
            self.advance()
            self.parse_expression()


# Example usage
if __name__ == "__main__":
    code = """
    check
    """

    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)

    try:
        parser.parse_program()
        print("Syntax OK!")
    except SyntaxError as e:
        print(str(e))
