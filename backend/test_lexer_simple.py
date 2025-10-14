#!/usr/bin/env python3

# Simple test script to verify the lexer works
import sys
sys.path.append('.')

from app.core.lexer import Lexer

# Test code
test_code = """
piece of y = 3;
piece of z = 10;
chars[] of name = "hello world";
"""

print("Testing Platter Lexer...")
print("Code to analyze:")
print(test_code)
print("\nTokens:")
print("-" * 50)

lexer = Lexer(test_code)
tokens = []

while True:
    token = lexer.get_next_token()
    if token is None:
        break
    print(f"{token.type:<15} | line={token.line:<3} | col={token.col:<3} | {token.value}")
    tokens.append(token)

print(f"\nTotal tokens: {len(tokens)}")