"""
Given a string, find the length of the longest substring
without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""

'''
"abcabcbb"
  |  |
{
    a: 0
    b: 1
    c: 2
'''

def longest_non_repeat(string):
    from collections import defaultdict
    if not string:
        return 0
    mapper = defaultdict(int)
    start, size = 0, 0
    for i, char in enumerate(string):
        if char not in mapper:
            mapper[char] = i
        elif char in mapper and mapper[char] >= start:
            size = max(size, i-start)
            start = mapper[char] + 1
            mapper[char] = i
    return max(size, i-start)

string = "pwwkew"
print(longest_non_repeat(string))
    
