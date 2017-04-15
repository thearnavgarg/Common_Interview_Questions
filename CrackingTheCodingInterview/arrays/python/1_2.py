'''
Time Complexity: O(n)
Space Complexity: O(n)
'''
def is_permutation(string1, string2):
	char_dict = {}
	# Filling our dictionary with the first string characters.
	for char in string1:
		if char in char_dict:
			char_dict[char] = char_dict[char]+1
		else:
			char_dict[char] = 1

	# Checking for the next string.
	for char in string2:
		# Checking if the char is on the dictionary.
		if char in char_dict:
			# removing one occurance of the character from the dictionary
			char_dict[char] = char_dict[char]-1
			# If no more occurances are left.. delete the key, value pair.
			if char_dict[char] == 0:
				del char_dict[char]
		else:
			return False

	if not char_dict:
		return True
	else:
		return False

def main():
	str1 = raw_input()
	str2 = raw_input()
	print ( is_permutation(str1, str2) )

if (__name__ == '__main__'):
	main()