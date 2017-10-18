import sys

"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271

123456789
124578 - 369
1257   - 48
127    - 5
"""

'''
Time Complexity: O(n^2)
Space Complexity: O(n) or O(1) [considering the list is already given]

'''

# this would convert my string input into a list.
def get_input_list(input):
	input_list = []
	for char in input:
		input_list.append((int)(char))
	return input_list

def circular_counter(input):
	input_list = get_input_list(input)
	skip = 2
	index = 0
	while(input_list):
		index = (skip + index) % len(input_list)
		print input_list.pop(index)
	

def main(args):
	input = raw_input()
	circular_counter(input)

if (__name__ == '__main__'):
	main(sys.argv)

