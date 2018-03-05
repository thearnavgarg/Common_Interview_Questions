'''
Write a function to find the longest common prefix string amongst an array of strings.

Leetcode: Your runtime beats 100.00 % of python3 submissions.
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        answer = []
        lengths = []
        for str in strs:
            lengths.append(len(str))
        minLen = min(lengths)
        for i in range(0, minLen):
            checker = True
            checkingChar = strs[0][i]
            for str in strs:
                if checkingChar == str[i]:
                    checker = True
                else:
                    checker = False
                    break
            if checker:
                answer.append(strs[0][i])
            else:
                break
        return ''.join(answer)       
        