from app.core.lexer import Lexer
from app.core.parser import Parser

from pprint import pprint

with open("./sample_programs/general.platter", "r", encoding="utf-8") as f:
    source = f.read()

lexer = Lexer(source)
tokens = lexer.tokenize()
print("TOKENS:")
pprint(tokens, indent=4, width=80)

parser = Parser(tokens)
ast = parser.parse_program()
print("AST:")
pprint(ast, indent=4, width=80)
