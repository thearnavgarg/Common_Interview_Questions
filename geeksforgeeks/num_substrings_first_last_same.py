'''
https://www.geeksforgeeks.org/recursive-solution-count-substrings-first-last-characters/
'''

'''
abcab



'''

def count_special_substrings(string) -> int:
    if not string:
        return 0
    counter = 0
    visited = set()
    for i in range(0, len(string)):
        substring = [string[i]]
        counter += 1
        for j in range(i+1, len(string)):
            substring.append(string[j])
            if substring[0] == substring[-1]:
                print(substring)
                counter += 1
                visited.add(''.join(substring))
    return counter

print(count_special_substrings('abcab'))