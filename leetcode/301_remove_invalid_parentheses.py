'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]

'''

def removeInvalidParentheses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    
    def parentheses_checker(s):
        left, right = 0, 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                right += 1
            if right > left:
                return False
        if left != right:
            return False
        return True
    
    
    if not s:
        return [""]
    
    stack = {s}
    res = []
    
    while True:
        res = list(filter(parentheses_checker, list(stack)))
        if res:
            return res
        temp = []
        print(stack)
        for s in stack:
            for i in range(len(s)):
                temp.append(s[:i]+s[i+1:])
        stack = set(temp)
    
    return [""]
