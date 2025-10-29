import pytest
from src.pattern_matcher import PatternMatcher
from src.token_definitions import Token, TokenType

def test_pattern_matcher_initialization():
    matcher = PatternMatcher()
    assert matcher.identifier_pattern is not None
    assert matcher.number_pattern is not None
    assert matcher.string_pattern is not None

def test_identifier_pattern():
    matcher = PatternMatcher()
    # Test valid identifiers
    valid_identifiers = [
        "variable",
        "test123",
        "_private",
        "camelCase",
        "UPPERCASE"
    ]
    
    for identifier in valid_identifiers:
        token = matcher.match_pattern(identifier, 1, 1)
        assert token is not None
        assert token.type == TokenType.IDENTIFIER
        assert token.value == identifier

def test_number_pattern():
    matcher = PatternMatcher()
    # Test valid numbers
    test_cases = [
        ("42", "42"),
        ("3.14", "3.14"),
        ("0", "0"),
        ("123.456", "123.456")
    ]
    
    for number, expected in test_cases:
        token = matcher.match_pattern(number, 1, 1)
        assert token is not None
        assert token.type == TokenType.NUMBER
        assert token.value == expected

def test_string_pattern():
    matcher = PatternMatcher()
    # Test string literals
    test_cases = [
        ('"Hello"', "Hello"),
        ('"Test String"', "Test String"),
        ('""', "")  # Empty string
    ]
    
    for string, expected in test_cases:
        token = matcher.match_pattern(string, 1, 1)
        assert token is not None
        assert token.type == TokenType.STRING
        assert token.value == expected

def test_comment_handling():
    matcher = PatternMatcher()
    # Test single-line comments
    single_line = "# This is a comment"
    token = matcher.handle_comment(single_line, 1, 1)
    assert token is None  # Comments should be ignored
    
    # Test multi-line comments
    multi_line = '"""This is a\nmulti-line\ncomment"""'
    token = matcher.handle_comment(multi_line, 1, 1)
    assert token is None  # Comments should be ignored
