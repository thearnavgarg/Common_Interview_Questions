'''
@author: Arnav Garg

Time Complexity: O(n) where n is the size of the input. 
'''
def urlify(string, truelen):
	string = string[:truelen]
	string_list = string.split(' ')
	temp_list = []
	for i in xrange(0, len(string_list)-1):
		temp_list.append(string_list[i])
		temp_list.append('%20')
	i = len(string_list)-1
	temp_list.append(string_list[i])
	return ''.join(temp_list)

def main():
	string = raw_input()
	truelen = int(raw_input())
	print ( urlify(string, truelen) )

if (__name__ == '__main__'):
	main()