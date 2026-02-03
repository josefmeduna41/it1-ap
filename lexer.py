from enum import Enum

grammar = """
plus = '+'
minus = '-'
number = REGEX("^[1-9]\d*$")
"""

class Token(Enum):
    INT = 0
    PLUS = 1
    MINUS = 2

class Lexer:
    src: str
    off: int

    def __init__(self, src: str) -> None:
        self.src = src
        self.off = 0

    def __iter__(self) -> 'Lexer':
        return self
    
    def __next__(self) -> Token:
        if len(self.src) >= self.off:
             raise StopIteration

         