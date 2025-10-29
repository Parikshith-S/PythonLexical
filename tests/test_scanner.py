import pytest
from src.scanner import Scanner
from src.token_definitions import Token, TokenType

def test_scanner_initialization():
    source = "test code"
    scanner = Scanner(source)
    assert scanner.source == source
    assert scanner.tokens == []
    assert scanner.start == 0
    assert scanner.current == 0
    assert scanner.line == 1
    assert scanner.column == 1

def test_is_at_end():
    scanner = Scanner("test")
    assert not scanner.is_at_end()
    scanner.current = 4  # Length of "test"
    assert scanner.is_at_end()

def test_advance():
    scanner = Scanner("abc")
    assert scanner.advance() == "a"
    assert scanner.current == 1
    assert scanner.column == 2
    assert scanner.advance() == "b"
    assert scanner.current == 2
    assert scanner.column == 3

def test_empty_source():
    scanner = Scanner("")
    tokens = scanner.scan_tokens()
    assert len(tokens) == 1
    assert tokens[0].type == TokenType.EOF

def test_whitespace_handling():
    scanner = Scanner("   \t\n   ")
    tokens = scanner.scan_tokens()
    assert len(tokens) == 1  # Only EOF token
    assert tokens[0].type == TokenType.EOF
    assert scanner.line == 2  # Due to newline character
