'''
Time complexity: O(n)
'''
def palindrome_permutation(string):
	my_dict = {}
	odd_tracker = 0
	# going over each value and adding it to the dictionary.
	for char in string:
		if char == ' ':
			continue
		if char in my_dict:
			my_dict[char] = my_dict[char] + 1
			if (my_dict[char] % 2 != 0):
				odd_tracker += 1
			else:
				odd_tracker -= 1
		else:
			my_dict[char] = 1
			odd_tracker += 1
	if (odd_tracker > 1):
		return False
	else:
		return True

	

def main():
	string = raw_input().lower()
	print( palindrome_permutation(string) )

if (__name__ == '__main__'):
	main()