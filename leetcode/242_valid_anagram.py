'''

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    from collections import defaultdict
    d = defaultdict(int)
    
    if len(s) != len(t) or set(s) != set(t):
        return False
    
    for char in s:
        d[char] += 1
    
    for char in t:
        d[char] -= 1
        if d[char] < 0:
            return False
    return True