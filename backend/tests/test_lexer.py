from app.core.lexer import Lexer

from pprint import pprint

with open("./sample_programs/general.platter", "r", encoding="utf-8") as f:
    source = f.read()

lexer = Lexer(source)
tokens = lexer.tokenize()
print("TOKENS:")
pprint(tokens, indent=4, width=80)