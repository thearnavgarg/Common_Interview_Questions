def generate_helper(parentheses, n, left, right, result):
    if len(parentheses) == 2*n:
        result.append(parentheses)
        return
    if left < n:
        generate_helper(parentheses+'(', n, left+1, right, result)
    if left > right:
        generate_helper(parentheses+')', n, left, right+1, result)
    return
    
    
def generate_parentheses(n):
    if n == 0:
        return []
    
    result = []
    parentheses = ''
    left, right = 0, 0
    generate_helper(parentheses, n, left, right, result)
    return result

print(generate_parentheses(3))