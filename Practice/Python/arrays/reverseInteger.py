'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows. 

Leetcode: Your runtime beats 100.00 % of python3 submissions
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        xString = str(x)
        isNegative = False
        if xString[0] == '-':
            isNegative = True
            xString = xString[1:]
        else:
            isNegative = False
        ans = []
        foundNonZero = False
        for i in range(len(xString)-1, -1,-1):
            if xString[i] == '0' and not foundNonZero:
                continue
            foundNonZero = True
            ans.append(xString[i])
        ansString = ''
        if isNegative:
            ansString = '-' + ''.join(ans)
        else:
            ansString = ''.join(ans)
        result = int(ansString)
        if result > 2147483647 or result < -2147483647:
            return 0
        else:
            return result