# 04
# Hard

# Given an arithmetic expression with *, /, - & + operators and single digit numbers, evaluate it and 
# return the result. The expression can also contain parenthesis.

# For example,
# 1 + 2 / 1 + 3 * 2 ⇒ 9
# 1  + (1 + 3) * 2 ⇒ 9
# 1 + 2 / (1 + 3) * 2 ⇒ 2


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(n) because we store a copy of the operator/operands in the stacks

ops_priorities = {'(':-1, '*':1, '/':1, '+':0, '-':0}

def process_expression(exp: str) -> float:
    operators = []
    operands = []
    for c in exp:
        if c == ' ':
            continue
        if c == '(':
            operators.append(c)
        elif c == ')':
            while operators[len(operators)-1] != '(':
                v = calculate(operators.pop(), operands.pop(), operands.pop())
                operands.append(v)
            operators.pop()
        elif c in ops_priorities:
            op_priority = ops_priorities[c]
            while operators and op_priority <= ops_priorities[operators[len(operators)-1]]:
                v = calculate(operators.pop(), operands.pop(), operands.pop())
                operands.append(v)
            operators.append(c)
        else:
            operands.append(int(c))
    while operators:
        v = calculate(operators.pop(), operands.pop(), operands.pop())
        operands.append(v)
    return operands.pop()

def calculate(operator: str, right_operand: float, left_operand: float) -> float:
    if operator == "*":
        return left_operand * right_operand
    if operator == "/":
        return left_operand / right_operand
    if operator == "+":
        return left_operand + right_operand
    if operator == "-":
        return left_operand - right_operand

# -----------------------------------------------------

import pytest

def test_process_expression():
    assert(process_expression('1 + 2 / 1 + 3 * 2') == 9)
    assert(process_expression('1  + (1 + 3) * 2') == 9)
    assert(process_expression('1 + 2 / (1 + 3) * 2') == 2)
    assert(process_expression('4 * 2 + (3 + 1) / 2') == 10)

pytest.main()
