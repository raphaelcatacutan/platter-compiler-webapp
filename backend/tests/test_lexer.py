
from pprint import pprint

from app.core.lexer2 import Lexer

with open("./tests/sample_programs/lexer_2.platter", "r", encoding="utf-8") as f:
    source = f.read()

lexer = Lexer(source)
tokens = lexer.tokenize()
print("TOKENS:")
pprint(tokens, indent=4, width=80)