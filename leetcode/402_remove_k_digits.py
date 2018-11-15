
'''
Given a non-negative integer num represented as a string, 
remove k digits from the number so that the new number is 
the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to 
form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. 
Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is 
left with nothing which is 0.
'''
class Solution:
    def removeKdigits(self, nums, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if not nums:
            return "0"
        
        if len(nums) <= k:
            return "0"
        
        nums = list(nums)
        current = 0
        while True:
            if k == 0:
                return str(int(''.join(nums)))
            if current == len(nums)-1:
                del nums[current]
                current -= 1
                k -= 1
            else:
                if int(nums[current]) > int(nums[current+1]):
                    del nums[current]
                    current = max(0, current-1)
                    k -= 1
                else:
                    current += 1
        return ''.join(nums)