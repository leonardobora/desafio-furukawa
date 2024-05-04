def is_balanced(expression):
    """
    Checks if the given expression has balanced brackets.

    Args:
        expression (str): The expression to be checked.

    Returns:
        bool: True if the expression has balanced brackets, False otherwise.
    """

    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return False

    return not stack


# Verifica se a expressão é balanceada
expression = input("Enter a mathematical expression: ")

if is_balanced(expression):
    print("The expression is balanced.")
else:
    print("The expression is not balanced.")

# Test case 1: Balanced expression
expression1 = "((2 + 3) * [4 - 5])"
assert is_balanced(expression1) == True

# Test case 2: Unbalanced expression
expression2 = "((2 + 3) * [4 - 5)"
assert is_balanced(expression2) == False

# Test case 3: Empty expression
expression3 = ""
assert is_balanced(expression3) == True

# Test case 4: Expression with no brackets
expression4 = "2 + 3"
assert is_balanced(expression4) == True