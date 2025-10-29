# Assigned to: Parikshith
# Responsibility: Token Definition and Management

from enum import Enum
from dataclasses import dataclass
from typing import Optional

class TokenType(Enum):
    # Keywords
    IF = "IF"
    ELSE = "ELSE"
    WHILE = "WHILE"
    FOR = "FOR"
    DEF = "DEF"
    CLASS = "CLASS"
    RETURN = "RETURN"
    
    # Operators
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    ASSIGN = "ASSIGN"
    
    # Delimiters
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    
    # Others
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    STRING = "STRING"
    NEWLINE = "NEWLINE"
    EOF = "EOF"

@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int
    
    def __str__(self) -> str:
        return f"Token({self.type}, '{self.value}', line={self.line}, col={self.column})"

# TODO: Implement methods for token comparison and validation
# TODO: Add support for additional token types as needed
# TODO: Implement token position tracking utilities
