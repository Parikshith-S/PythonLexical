# Assigned to: Raj
# Responsibility: Scanner/Tokenizer Core

from typing import List, Optional
from token_definitions import Token, TokenType

class Scanner:
    def __init__(self, source: str):
        self.source = source
        self.tokens: List[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.column = 1

    def scan_tokens(self) -> List[Token]:
        """
        Main method to scan the source code and produce tokens.
        Returns a list of tokens.
        """
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        
        self.tokens.append(Token(TokenType.EOF, "", self.line, self.column))
        return self.tokens

    def scan_token(self):
        """
        Scan a single token.
        TODO: Implement the scanning logic for different token types
        """
        char = self.advance()
        # TODO: Implement basic token scanning logic
        # TODO: Add switch-case like structure for different characters
        # TODO: Handle basic tokens like operators and delimiters

    def is_at_end(self) -> bool:
        """Check if we've reached the end of source code."""
        return self.current >= len(self.source)

    def advance(self) -> str:
        """Advance current pointer and return current character."""
        char = self.source[self.current]
        self.current += 1
        self.column += 1
        return char

    # TODO: Implement helper methods for peeking and matching characters
    # TODO: Implement methods for handling whitespace and newlines
    # TODO: Add basic token recognition logic
