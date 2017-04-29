"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
give a single resultant array.

function flatten(input){
}

Example:

Input: var input = [2, 1, [3, [4, 5], 6], 7, [8]];
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]
"""

def flatten_array(input, result):
	for i in input:
		if (type(i) is int):
			result.append(i)
		if (type(i) is list):
			flatten_array(i, result)	# recursive call to the function for
										# inner list.
	return result

def main():
	input = [2, 1, [3, [4, 5], 6], 7, [8]]
	result = []
	result = flatten_array(input, result)
	print result

if __name__ == '__main__':
	main()

'''
Explanation:
------------

Check if the element present is a integer or not..
if the element present turns out to be a list, then recursively,
call the function again to check the list for the numbers in it.

'''