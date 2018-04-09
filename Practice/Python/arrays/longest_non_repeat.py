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

def longest_non_repeat(string):
    if not string:
        return 0
    char2idx = {}
    start = 0
    max_len = 0
    for idx, ele in enumerate(string):
        if not ele in char2idx.keys():
            char2idx[ele] = idx
        else:
            if start <= char2idx[ele]:
                start = char2idx[ele] + 1
            char2idx[ele] = idx
        max_len = max(max_len, (idx-start+1))
    return max_len

def main():
    string = 'abcabcbb'
    print(longest_non_repeat(string))


if __name__ == '__main__':
    main()