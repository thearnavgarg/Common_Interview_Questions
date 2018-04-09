"""
Given an array S of n integers, are there elements a, b, c in S
such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
{
  (-1, 0, 1),
  (-1, -1, 2)
}
"""

'''
scratch work
------------

INPUT: [-1, 0, 1, 2, -1, -4]
OUTPUT: {
  (-1, 0, 1),
  (-1, -1, 2)
}

[-4, -1, -1, 0, 1, 2]
'''

def three_sum(arr):
  if not arr:
    return None
  res = set()
  arr.sort()
  for i in range(0, len(arr)-2):
    # if i > 0 and arr[i] == arr[i-1]:
    #   continue
    left = i+1
    right = len(arr)-1
    while left < right:
      sum = arr[i] + arr[left] + arr[right]
      if sum > 0:
        right = right - 1
      elif sum < 0:
        left = left + 1
      else:
        answer = (arr[i], arr[left], arr[right])
        res.add(answer)
        break
  return res


def main():
  arr = [-1, 0, 1, 2, -1, -4]
  print(three_sum(arr))

main()