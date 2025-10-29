# Main lexical analyzer that integrates all components

from src.token_definitions import Token, TokenType
from src.scanner import Scanner
from src.pattern_matcher import PatternMatcher

class LexicalAnalyzer:
    def __init__(self, source_code: str):
        self.scanner = Scanner(source_code)
        self.pattern_matcher = PatternMatcher()

    def analyze(self):
        """
        Perform lexical analysis on the source code
        Returns a list of tokens
        """
        return self.scanner.scan_tokens()

def main():
    # Example usage
    source_code = """
    def example():
        x = 42
        print("Hello, World!")
    """
    
    lexer = LexicalAnalyzer(source_code)
    tokens = lexer.analyze()
    
    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()
