# Python Lexical Analyzer

A collaborative lexical analyzer project that tokenizes Python source code into meaningful tokens. This project is divided among three team members, each responsible for specific components of the lexical analyzer.

## Team Members and Responsibilities

### 1. Parikshith - Token Definition and Management
**File:** `src/token_definitions.py`
- Define and implement all token types (keywords, operators, identifiers, etc.)
- Create and manage the Token class structure
- Implement token attributes (type, value, position tracking)
- Handle token validation and comparison methods

Key responsibilities:
- Defining token types using Python''s Enum
- Implementing the Token dataclass
- Managing token position information (line, column)
- Implementing token utility methods

### 2. Raj - Scanner/Tokenizer Core
**File:** `src/scanner.py`
- Implement the core scanning logic
- Manage character stream processing
- Handle basic tokenization
- Track line and column numbers

Key responsibilities:
- Character stream management
- Position tracking in source code
- Basic token recognition
- Implementing scanner helper methods

### 3. Jeevana - Pattern Matching and Special Cases
**File:** `src/pattern_matcher.py`
- Implement regex-based pattern matching
- Handle complex tokens (strings, comments)
- Manage error detection and reporting
- Handle special cases and edge conditions

Key responsibilities:
- Regular expression pattern implementation
- String literal processing
- Comment handling (single-line and multi-line)
- Error detection and reporting

## Project Structure
```
PythonLexical/
├── src/
│   ├── token_definitions.py  (Parikshith)
│   ├── scanner.py           (Raj)
│   ├── pattern_matcher.py   (Jeevana)
│   └── main.py             (Integration)
├── tests/
│   ├── test_token_definitions.py
│   ├── test_scanner.py
│   ├── test_pattern_matcher.py
│   └── test_integration.py
├── README.md
└── pyproject.toml
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Clone the Repository
```bash
git clone https://github.com/Parikshith-S/PythonLexical.git
cd PythonLexical
```

### Set Up Development Environment
1. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

2. Install required packages:
```bash
pip install pytest
```

### Running the Project
1. Run the main program:
```bash
python src/main.py
```

2. Run the tests:
```bash
pytest tests/
```

## Development Workflow

### For Team Members
1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Implement your assigned component:
- Parikshith: Work on `token_definitions.py`
- Raj: Work on `scanner.py`
- Jeevana: Work on `pattern_matcher.py`

3. Write tests for your component:
- Use the corresponding test file in the `tests/` directory
- Follow the existing test patterns
- Ensure all tests pass before committing

4. Commit your changes:
```bash
git add .
git commit -m "Description of your changes"
git push origin feature/your-feature-name
```

5. Create a pull request when your component is ready for review

### Testing Your Code
- Run specific test file:
```bash
pytest tests/test_your_component.py
```

- Run all tests:
```bash
pytest tests/
```

- Run tests with detailed output:
```bash
pytest -v tests/
```

## Integration
The `main.py` file demonstrates how all components work together. Use this file to test the complete lexical analyzer:

```python
from src.main import LexicalAnalyzer

source_code = """
def example():
    x = 42
    print("Hello, World!")
"""

lexer = LexicalAnalyzer(source_code)
tokens = lexer.analyze()
for token in tokens:
    print(token)
```

## Best Practices
1. Follow PEP 8 style guidelines
2. Write clear docstrings and comments
3. Keep methods focused and single-purpose
4. Write tests for new functionality
5. Update documentation as needed

## Documentation Guidelines
- Use docstrings for all classes and methods
- Include type hints
- Document parameters and return values
- Add usage examples in docstrings

## Common Issues and Solutions
1. Token Recognition Issues
   - Check the pattern matcher implementation
   - Verify regex patterns
   - Review scanner position tracking

2. Error Handling
   - Use descriptive error messages
   - Include line and column numbers
   - Implement proper error recovery

3. Testing Issues
   - Ensure virtual environment is activated
   - Verify pytest installation
   - Check test file naming convention

## Contributing
1. Follow the assigned component responsibilities
2. Write tests for new features
3. Update documentation as needed
4. Create descriptive pull requests
5. Review team members code

## Contact Information
- Parikshith: [Contact Info]
- Raj: [Contact Info]
- Jeevana: [Contact Info]

## Project Timeline
- Development Phase: [Dates]
- Testing Phase: [Dates]
- Integration Phase: [Dates]
- Final Review: [Dates]
