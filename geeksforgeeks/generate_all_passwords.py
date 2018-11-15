'''
https://www.geeksforgeeks.org/generate-passwords-given-character-set/
'''

def generate_passwords(chars, max_len):

    def helper(chars, max_len, password, current):
        if current:
            password.add(''.join(current))
        if max_len == 0:
            return
        for i in range(0, len(chars)):
            current.append(chars[i])
            helper(chars, max_len-1, password, current)
            current.pop()

    if not chars:
        return []
    passwords = set()
    current = []
    helper(chars, max_len, passwords, current)
    return list(passwords)

chars = ['a', 'b']
max_len = 2
print(generate_passwords(chars, max_len))
