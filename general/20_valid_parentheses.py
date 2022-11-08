"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""


def is_valid(s: str) -> bool:
    stack = []
    parens = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    for char in s:
        # If opens. Then adds to the stack.
        if char in parens:
            stack.append(char)
            continue
        # This is not a open bracket.
        # If opposites the last element, then pop the last element.
        if len(stack) == 0:
            return False
        last_element = stack[-1]
        if char == parens.get(last_element):
            stack.pop()
            continue
        stack.append(char)
    return not stack


if __name__ == '__main__':
    assert(is_valid('()') == True)
    assert(is_valid('()[]{}') == True)
    assert(is_valid('(]') == False)
    assert(is_valid('(((())))') == True)
    assert(is_valid('(((()))') == False)
    assert(is_valid('([]){}') == True)
    assert(is_valid(']') == False)