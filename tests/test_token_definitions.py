import pytest
from src.token_definitions import (
    Token, TokenType, Position,
    create_keyword_token, create_operator_token, create_delimiter_token
)

# Position Tests
def test_position_creation_and_advancement():
    pos = Position(1, 1)
    assert pos.line == 1
    assert pos.column == 1
    
    # Test advancement
    pos.advance('a')
    assert pos.column == 2
    assert pos.line == 1
    
    pos.advance('\n')
    assert pos.line == 2
    assert pos.column == 0
    
    # Test position copy
    pos_copy = pos.copy()
    assert pos_copy.line == pos.line
    assert pos_copy.column == pos.column
    assert pos_copy is not pos

# Token Creation and Basic Properties Tests
def test_token_creation():
    pos = Position(1, 5)
    token = Token(TokenType.IDENTIFIER, "variable", pos.line, pos.column, pos)
    assert token.type == TokenType.IDENTIFIER
    assert token.value == "variable"
    assert token.line == 1
    assert token.column == 5
    assert token.position is pos

def test_token_string_representation():
    pos = Position(1, 10)
    token = Token(TokenType.NUMBER, "42", pos.line, pos.column, pos)
    expected = "Token(TokenType.NUMBER, '42' @ line 1, column 10)"
    assert str(token) == expected

# Token Classification Tests
def test_token_classification():
    pos = Position(1, 1)
    
    # Test keyword classification
    keyword_token = Token(TokenType.IF, "if", 1, 1, pos)
    assert keyword_token.is_keyword
    assert not keyword_token.is_operator
    assert not keyword_token.is_delimiter
    
    # Test operator classification
    operator_token = Token(TokenType.PLUS, "+", 1, 1, pos)
    assert operator_token.is_operator
    assert not operator_token.is_keyword
    assert not operator_token.is_delimiter
    
    # Test delimiter classification
    delimiter_token = Token(TokenType.LPAREN, "(", 1, 1, pos)
    assert delimiter_token.is_delimiter
    assert not delimiter_token.is_keyword
    assert not delimiter_token.is_operator

# Token Validation Tests
def test_token_validation():
    pos = Position(1, 1)
    
    # Test number validation
    valid_number = Token(TokenType.NUMBER, "42.5", 1, 1, pos)
    invalid_number = Token(TokenType.NUMBER, "4x2", 1, 1, pos)
    assert valid_number.validate()
    assert not invalid_number.validate()
    
    # Test string validation
    valid_string = Token(TokenType.STRING, '"hello"', 1, 1, pos)
    invalid_string = Token(TokenType.STRING, 'hello', 1, 1, pos)
    assert valid_string.validate()
    assert not invalid_string.validate()
    
    # Test identifier validation
    valid_identifier = Token(TokenType.IDENTIFIER, "valid_name", 1, 1, pos)
    invalid_identifier = Token(TokenType.IDENTIFIER, "123invalid", 1, 1, pos)
    assert valid_identifier.validate()
    assert not invalid_identifier.validate()

# Token Factory Function Tests
def test_create_keyword_token():
    pos = Position(1, 1)
    
    # Test known keyword
    if_token = create_keyword_token("if", pos)
    assert if_token.type == TokenType.IF
    assert if_token.value == "if"
    
    # Test unknown keyword (should create identifier)
    unknown_token = create_keyword_token("unknown", pos)
    assert unknown_token.type == TokenType.IDENTIFIER
    assert unknown_token.value == "unknown"

def test_create_operator_token():
    pos = Position(1, 1)
    
    # Test simple operators
    plus_token = create_operator_token("+", pos)
    assert plus_token and plus_token.type == TokenType.PLUS
    
    # Test compound operators
    plus_assign_token = create_operator_token("+=", pos)
    assert plus_assign_token and plus_assign_token.type == TokenType.PLUSASSIGN
    
    # Test invalid operator
    invalid_operator = create_operator_token("@", pos)
    assert invalid_operator is None

def test_create_delimiter_token():
    pos = Position(1, 1)
    
    # Test basic delimiters
    lparen_token = create_delimiter_token("(", pos)
    assert lparen_token and lparen_token.type == TokenType.LPAREN
    
    # Test invalid delimiter
    invalid_delimiter = create_delimiter_token("?", pos)
    assert invalid_delimiter is None

# Token Comparison Tests
def test_token_comparison():
    pos = Position(1, 1)
    token1 = Token(TokenType.NUMBER, "42", 1, 1, pos)
    token2 = Token(TokenType.NUMBER, "42", 1, 1, pos.copy())
    token3 = Token(TokenType.NUMBER, "43", 1, 1, pos.copy())
    
    assert token1 == token2
    assert token1 != token3
    
    # Test matches method
    assert token1.matches(TokenType.NUMBER)
    assert token1.matches(TokenType.NUMBER, "42")
    assert not token1.matches(TokenType.STRING)
    assert not token1.matches(TokenType.NUMBER, "43")
