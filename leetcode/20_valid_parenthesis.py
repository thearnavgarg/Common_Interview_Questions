'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    
    def is_open_bracket(char):
        if char in '({[':
            return True
        return False
    
    def is_close_bracket(char):
        if char in ')}]':
            return True
        return False
    
    def is_same(open_bracket, close_bracket):
        bracket = open_bracket + close_bracket
        if bracket in {'{}', '[]', '()'}:
            return True
        return False
    
    
    if not s:
        return True
    
    stack = []
    
    for char in s:
        if is_open_bracket(char):
            stack.append(char)
        elif is_close_bracket(char):
            if not stack:
                return False
            bracket = stack.pop()
            if not is_same(bracket, char):
                return False
    if stack:
        return False
    return True