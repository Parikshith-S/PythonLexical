import pytest
from src.main import LexicalAnalyzer
from src.token_definitions import TokenType

def test_lexical_analyzer_initialization():
    source = "test code"
    analyzer = LexicalAnalyzer(source)
    assert analyzer.scanner is not None
    assert analyzer.pattern_matcher is not None

def test_basic_program_analysis():
    source = """
def main():
    x = 42
    print("Hello")
    """
    
    analyzer = LexicalAnalyzer(source)
    tokens = analyzer.analyze()
    
    # Check if basic tokens are present
    token_types = [token.type for token in tokens]
    
    assert TokenType.DEF in token_types
    assert TokenType.IDENTIFIER in token_types  # for 'main', 'print'
    assert TokenType.NUMBER in token_types      # for '42'
    assert TokenType.STRING in token_types      # for "Hello"
    assert TokenType.EOF in token_types

def test_empty_program():
    analyzer = LexicalAnalyzer("")
    tokens = analyzer.analyze()
    assert len(tokens) == 1
    assert tokens[0].type == TokenType.EOF

def test_complex_expression():
    source = "result = (40 + 2) * 3"
    analyzer = LexicalAnalyzer(source)
    tokens = analyzer.analyze()
    
    expected_types = [
        TokenType.IDENTIFIER,  # result
        TokenType.ASSIGN,      # =
        TokenType.LPAREN,      # (
        TokenType.NUMBER,      # 40
        TokenType.PLUS,        # +
        TokenType.NUMBER,      # 2
        TokenType.RPAREN,      # )
        TokenType.MULTIPLY,    # *
        TokenType.NUMBER,      # 3
        TokenType.EOF
    ]
    
    assert len(tokens) == len(expected_types)
    for token, expected_type in zip(tokens, expected_types):
        assert token.type == expected_type
