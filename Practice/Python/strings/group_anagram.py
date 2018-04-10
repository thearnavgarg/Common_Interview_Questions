"""
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

'''
'''

def group_anagram(strings):
    # return the array of groups of anagram
    d = {}
    for string in strings:
        sstring = ''.join(sorted(string))
        if sstring in d:
            d[sstring].append(string)
        else:
            d[sstring] = []
            d[sstring].append(string)
    result = []
    for key, value in d.items():
        result.append(value)
    return result

def main():
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagram(strings))

main()