# 03
# Hard

# Given an arithmetic expression with *, /, - & + operators and single digit numbers, 
# evaluate it and return the result. 

# For example, 1 + 2 / 1 + 3 * 2 ==> 9


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(n) because we store a copy of the operator/operands in the stacks

ops_priorities = {'*':1, '/':1, '+':0, '-':0}

def stack_math(exp: str) -> float:
    operands = []
    operators = []
    for c in exp:
        if c == ' ':
            continue
        # print(f"operands={operands} operators={operators}")
        # print(f"c={c}")
        if c in ops_priorities:
            if not operators:
                operators.append(c)
                continue
            while operators and ops_priorities[c] <= ops_priorities[operators[len(operators)-1]]:
                op = operators.pop()
                v = calculate(op, operands.pop(), operands.pop())
                operands.append(v)
                # print(f"--> operands={operands} operators={operators}")
            operators.append(c)
        else:
            operands.append(int(c))
    while operators:
        op = operators.pop()
        v = calculate(op, operands.pop(), operands.pop())
        operands.append(v)
        # print(f"----> operands={operands} operators={operators}")
    return operands.pop()

def calculate(operator: str, right_operand: float, left_operand: float) -> float:
    if operator == '*':
        return left_operand * right_operand
    if operator == '/':
        return left_operand / right_operand
    if operator == '+':
        return left_operand + right_operand
    if operator == '-':
        return left_operand - right_operand

# -----------------------------------------------------

import pytest

def test_stack_math():
    assert(stack_math('1 + 2 / 1 + 3 * 2') == 9)
    assert(stack_math('3 * 8 / 2 - 5 * 2') == 2)
    assert(stack_math('2 * 5 + 7 * 3 - 9 / 3 - 7 * 2') == 14)

pytest.main()
