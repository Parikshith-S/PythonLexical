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
    IMPORT = "IMPORT"
    FROM = "FROM"
    AS = "AS"
    TRY = "TRY"
    EXCEPT = "EXCEPT"
    FINALLY = "FINALLY"
    RAISE = "RAISE"
    
    # Operators
    PLUS = "PLUS"              # +
    MINUS = "MINUS"            # -
    MULTIPLY = "MULTIPLY"      # *
    DIVIDE = "DIVIDE"          # /
    MODULO = "MODULO"         # %
    POWER = "POWER"           # **
    ASSIGN = "ASSIGN"         # =
    PLUSASSIGN = "PLUSASSIGN" # +=
    MINUSASSIGN = "MINUSASSIGN" # -=
    EQUALS = "EQUALS"         # ==
    NOTEQUALS = "NOTEQUALS"   # !=
    GREATER = "GREATER"       # >
    LESS = "LESS"            # <
    GREATEREQUAL = "GREATEREQUAL" # >=
    LESSEQUAL = "LESSEQUAL"   # <=
    
    # Delimiters
    LPAREN = "LPAREN"         # (
    RPAREN = "RPAREN"         # )
    LBRACE = "LBRACE"         # {
    RBRACE = "RBRACE"         # }
    LBRACKET = "LBRACKET"     # [
    RBRACKET = "RBRACKET"     # ]
    COMMA = "COMMA"           # ,
    DOT = "DOT"              # .
    COLON = "COLON"          # :
    SEMICOLON = "SEMICOLON"   # ;
    
    # Others
    IDENTIFIER = "IDENTIFIER" # Variable names, function names, etc.
    NUMBER = "NUMBER"         # Integers and floating-point numbers
    STRING = "STRING"         # String literals
    COMMENT = "COMMENT"       # Single and multi-line comments
    NEWLINE = "NEWLINE"      # Line breaks
    INDENT = "INDENT"        # Increase in indentation
    DEDENT = "DEDENT"        # Decrease in indentation
    EOF = "EOF"              # End of file marker

class Position:
    """Tracks position in source code, including file, line, and column information."""
    def __init__(self, line: int, column: int, index: int = 0, filename: str = "<unknown>"):
        self.line = line
        self.column = column
        self.index = index
        self.filename = filename

    def advance(self, current_char: str = "") -> 'Position':
        """Advance position based on the current character."""
        self.index += 1
        self.column += 1

        if current_char == '\n':
            self.line += 1
            self.column = 0

        return self

    def copy(self) -> 'Position':
        """Create a copy of the current position."""
        return Position(
            self.line,
            self.column,
            self.index,
            self.filename
        )

    def __str__(self) -> str:
        return f"line {self.line}, column {self.column}"

@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int
    position: Optional[Position] = None

    @property
    def is_keyword(self) -> bool:
        """Check if the token is a keyword."""
        return self.type.name in [
            'IF', 'ELSE', 'WHILE', 'FOR', 'DEF', 'CLASS', 'RETURN',
            'IMPORT', 'FROM', 'AS', 'TRY', 'EXCEPT', 'FINALLY', 'RAISE'
        ]

    @property
    def is_operator(self) -> bool:
        """Check if the token is an operator."""
        return self.type.name in [
            'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MODULO', 'POWER',
            'ASSIGN', 'PLUSASSIGN', 'MINUSASSIGN', 'EQUALS', 'NOTEQUALS',
            'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL'
        ]

    @property
    def is_delimiter(self) -> bool:
        """Check if the token is a delimiter."""
        return self.type.name in [
            'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
            'COMMA', 'DOT', 'COLON', 'SEMICOLON'
        ]

    def matches(self, token_type: TokenType, value: Optional[str] = None) -> bool:
        """Check if token matches a specific type and optionally a value."""
        if self.type != token_type:
            return False
        if value is not None and self.value != value:
            return False
        return True

    def validate(self) -> bool:
        """Validate token based on its type."""
        try:
            if self.type == TokenType.NUMBER:
                # Try parsing as float to validate number format
                float(self.value)
            elif self.type == TokenType.STRING:
                # Check if string is properly quoted
                if not (self.value.startswith('"') and self.value.endswith('"') or
                       self.value.startswith("'") and self.value.endswith("'")):
                    return False
            elif self.type == TokenType.IDENTIFIER:
                # Check identifier naming rules
                if not self.value.isidentifier():
                    return False
            return True
        except ValueError:
            return False

    def __str__(self) -> str:
        pos_str = f" @ {self.position}" if self.position else f", line={self.line}, col={self.column}"
        return f"Token({self.type}, '{self.value}'{pos_str})"

    def __eq__(self, other: object) -> bool:
        """Compare two tokens for equality."""
        if not isinstance(other, Token):
            return NotImplemented
        return (
            self.type == other.type and
            self.value == other.value and
            self.line == other.line and
            self.column == other.column
        )

# Utility functions for token operations
def create_keyword_token(keyword: str, position: Position) -> Token:
    """Create a token for a keyword."""
    try:
        token_type = TokenType[keyword.upper()]
        return Token(token_type, keyword, position.line, position.column, position)
    except KeyError:
        return Token(TokenType.IDENTIFIER, keyword, position.line, position.column, position)

def create_operator_token(operator: str, position: Position) -> Optional[Token]:
    """Create a token for an operator."""
    operator_map = {
        '+': TokenType.PLUS,
        '-': TokenType.MINUS,
        '*': TokenType.MULTIPLY,
        '/': TokenType.DIVIDE,
        '%': TokenType.MODULO,
        '**': TokenType.POWER,
        '=': TokenType.ASSIGN,
        '+=': TokenType.PLUSASSIGN,
        '-=': TokenType.MINUSASSIGN,
        '==': TokenType.EQUALS,
        '!=': TokenType.NOTEQUALS,
        '>': TokenType.GREATER,
        '<': TokenType.LESS,
        '>=': TokenType.GREATEREQUAL,
        '<=': TokenType.LESSEQUAL
    }
    
    if operator in operator_map:
        return Token(operator_map[operator], operator, position.line, position.column, position)
    return None

def create_delimiter_token(delimiter: str, position: Position) -> Optional[Token]:
    """Create a token for a delimiter."""
    delimiter_map = {
        '(': TokenType.LPAREN,
        ')': TokenType.RPAREN,
        '{': TokenType.LBRACE,
        '}': TokenType.RBRACE,
        '[': TokenType.LBRACKET,
        ']': TokenType.RBRACKET,
        ',': TokenType.COMMA,
        '.': TokenType.DOT,
        ':': TokenType.COLON,
        ';': TokenType.SEMICOLON
    }
    
    if delimiter in delimiter_map:
        return Token(delimiter_map[delimiter], delimiter, position.line, position.column, position)
    return None
