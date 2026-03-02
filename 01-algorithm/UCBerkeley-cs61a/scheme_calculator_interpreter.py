import operator
############################
# EXCEPTION
############################
class SchemeCalculatorError(Exception):
    """Base class for calculator errors."""
    def __init__(self, message, position=None):
        super().__init__(message)
        self.position = position

class InvalidSyntaxError(SchemeCalculatorError):
    """Invalid expression structure."""
    pass

"""Separation of concerns -- each stage (tokenizer, parser, & evaluator) should only check the error it is responsible for
Tokenizer: convert raw characters into valid tokens.
        - invalid characters
        - unmatched parentheses
Parser: build expression tree and valid structure.
        - operator must follow '('
        - empty parenthesis
Evaluator: compute result from tree
"""
# -------------------------
# Tokenization Errors
# -------------------------

class TokenizeError(SchemeCalculatorError):
    """Error while converting input string to tokens."""
    pass


class InvalidCharacterError(TokenizeError):
    """Character is not allowed."""
    pass


class ParenthesisMismatchError(TokenizeError):
    """Unmatched '(' or ')'."""
    pass


# -------------------------
# Parsing Errors
# -------------------------

class ParseError(SchemeCalculatorError):
    """Error while building syntax tree."""
    pass

class OperatorExpectedError(ParseError):
    """Expected operator after '('."""
    pass


class OperandExpectedError(ParseError):
    """Expected number but got something else."""
    pass


# -------------------------
# Evaluation Errors
# -------------------------

class EvaluationError(SchemeCalculatorError):
    """Error during evaluation."""
    pass


class DivisionByZeroError(EvaluationError):
    """Division by zero."""
    pass

############################
# TOKENIZER
############################
VALID_CHAR = ['+', '-', '*', '/', '(', ')', ' ', '.']
VALID_OPERATOR = ['+', '-', '*', '/']

def tokenize(source):
    """Return a list of tokens containing calculation expression elements in user input.
    >>> s = "(+ 3.456 (*   56 (- 8.9       11)))"
    >>> tokenize(s)
    ['(', '+', '3.456', '(', '*', '56', '(', '-', '8.9', '11', ')', ')', ')']
    """
    tokens = []
    paren_count = 0
    i = 0
    while i < len(source):
        c = source[i]
        if not (c.isdigit() or c in VALID_CHAR):    # Exception 1: check for invalid characters in user input
            raise InvalidCharacterError(f"Invalid character: {c}")
        if c == '.':
            raise InvalidSyntaxError("Invalid use of '.'")

        if c.isspace():    # if c is a space, skip current character
            i += 1
            continue
        
        if c.isdigit():
            number = c
            count = 1
            while i + count < len(source) and (source[i+count].isdigit() or source[i+count] == '.'):
                if source[i+count] == '.':
                    if not source[i+count+1].isdigit():
                        raise InvalidSyntaxError("Invalid use of '.'")
                number += source[i+count]
                count += 1
            tokens.append(number)
            i += count
            continue
        
        if c == '(':
            paren_count += 1
        
        if c == ')':
            paren_count -= 1
        
        tokens.append(c)
        i += 1

    if paren_count != 0:    # Exception 2: check for unmateched parentheses in user input
        raise ParenthesisMismatchError("Unmatched parenthesis")
    return tokens


############################
# PARSER
############################
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []
    def __repr__(self):
        if not self.children:
            return f"Node({self.value})"
        return f"Node({self.value}, {self.children})"

def is_number(s):
    """Return True if the containt of the string s is a number, False otherwise."""
    try:
        float(s)
        return True
    except ValueError:
        return False
    
# construct a AST expression tree on tokens
def parse(tokens):
    """Construct an AST expression tree based on tokens
    
    >>> s = "(+ 3.456 (*   56 (- 8.9       11)))"
    >>> tokenize(s)
    ['(', '+', '3.456', '(', '*', '56', '(', '-', '8.9', '11', ')', ')', ')']
    >>> parse(tokenize(s))
    Node(+, [Node(3.456), Node(*, [Node(56.0), Node(-, [Node(8.9), Node(11.0)])])])
    """

    if len(tokens) < 1:
        return
    
    v = tokens.pop(0)

    if v == '(':
        operator = tokens.pop(0)
        if not (operator in VALID_OPERATOR):
            raise OperandExpectedError("Missing or invalid operator")
        
        node = Node(operator)
        while tokens and tokens[0] != ')':
            child = parse(tokens)
            node.children.append(child)
        
        tokens.pop(0)       # remove ')' from tokens
        return node

    if v == ')':        # unexpected ')'
        raise ParenthesisMismatchError("Unexpected ')'")
    
    if is_number(v):
        return Node(float(v))


############################
# EVALUATOR
############################
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def evaluate(expr):
    """Return the result of computing an expression tree.

    >>> s = "(+ 3.456 (*   56 (- 8.9       11)))"
    >>> evaluate(parse(tokenize(s)))
    -144.144
    """
    v = expr.value
    if v in VALID_OPERATOR:
        f = OPERATORS[v]
        values = [evaluate(c) for c in expr.children]
        if v == '-' and len(values) == 1:
            return -values[0]

        if v == '/' and len(values) == 1:
            return 1 / values[0]

        result = values[0]
        for val in values[1:]:
            result = f(result, val)
        return round(result, 6)

    if is_number(v):
        return v

############################
# REPL
###########################
# def repl():
#     while True:
#         try:
#             user_input = input("scheme> ")
#             print("You typed:", user_input)
#             """
#             expr = input("scheme> ")
#             tokens = tokenize(expr)
#             tree = parse(tokens)
#             result = evaluate(tree)
#             print(result)
#             """
#         except (EOFError, KeyboardInterrupt):
#             print("\nExiting Scheme Calculator interpreter.")
#             break

# if __name__ == "__main__":
#     repl()