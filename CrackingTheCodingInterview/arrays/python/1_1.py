'''
Time Complexity (With Addtnl DS): O(n)
Space Complexity (With Addtnl DS): O(n)

Time Complexity (Without Addtnl DS): O(n)
Space Complexity (Without Addtnl DS): O(n)
'''

def without_addtnl_ds(string):
	# a,b,c ..... z
	# 0,1,2......26
	alpha_map = 26*[0]
	for char in string:
		ascii_val = ord(char.lower()) - ord('a') 
		if (alpha_map[ascii_val] == 1):
			return False
		else:
			alpha_map[ascii_val] = 1
	return True

def with_addtnl_ds(string):
    unique_dict = {}
    # for each char we check if it has already been seen before
    # and if it has, then return False.
    for char in string:
        if unique_dict.has_key(char):
        	return False
        else:
        	unique_dict[char] = 1
    return True

def main():
    input_string = raw_input()
    print ( with_addtnl_ds(input_string) )
    print ( without_addtnl_ds(input_string) )

if (__name__ == '__main__'):
    main()
