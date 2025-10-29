import pytest
from src.token_definitions import Token, TokenType

def test_token_creation():
    # Test basic token creation
    token = Token(TokenType.IDENTIFIER, "variable", 1, 5)
    assert token.type == TokenType.IDENTIFIER
    assert token.value == "variable"
    assert token.line == 1
    assert token.column == 5

def test_token_string_representation():
    # Test string representation of token
    token = Token(TokenType.NUMBER, "42", 1, 10)
    expected = "Token(TokenType.NUMBER, '42', line=1, col=10)"
    assert str(token) == expected

def test_keyword_tokens():
    # Test keyword token types
    keywords = [
        (TokenType.IF, "if"),
        (TokenType.ELSE, "else"),
        (TokenType.WHILE, "while"),
        (TokenType.FOR, "for"),
        (TokenType.DEF, "def"),
    ]
    
    for token_type, keyword in keywords:
        token = Token(token_type, keyword, 1, 1)
        assert token.type == token_type
        assert token.value == keyword

def test_operator_tokens():
    # Test operator token types
    operators = [
        (TokenType.PLUS, "+"),
        (TokenType.MINUS, "-"),
        (TokenType.MULTIPLY, "*"),
        (TokenType.DIVIDE, "/"),
        (TokenType.ASSIGN, "="),
    ]
    
    for token_type, operator in operators:
        token = Token(token_type, operator, 1, 1)
        assert token.type == token_type
        assert token.value == operator
