# There is a parking lot with only one empty spot. Given the initial state
# of the parking lot and the final state. Each step we are only allowed to
# move a car out of its place and move it into the empty spot.
# The goal is to find out the least movement needed to rearrange
# the parking lot from the initial state to the final state.

# Say the initial state is an array:

# [1,2,3,0,4],
# where 1,2,3,4 are different cars, and 0 is the empty spot.

# And the final state is

# [0,3,2,1,4].
# We can swap 1 with 0 in the initial array to get [0,2,3,1,4] and so on.
# Each step swap with 0 only.

'''
Scratch work

Initial state: 
[1,2,3,0,4] total displacement from the final state: 1, 2, 3, 4
[0,2,3,1,4]
[3,2,0,1,4]
[3,0,2,1,4]
[0,3,2,1,4]
------------
[0,3,2,1,4]

 0 1 2 3 4
[1,2,3,0,4]
[0,3,2,1,4]

set(0,1) and set(1,0)

[1,2,3,4,0]
[0,1,2,3,4]

Final state: 
'''

def main():
	initial = [1,2,3,0,4]
	final = [0,3,2,1,4]
	steps = 0
	if len(initial) != len(final):
		print '-1'
		return
	i = 0
	while(i < len(initial)):
		if initial[i] != final[i]:
			steps += 1
		i += 1
	print steps

if __name__ == '__main__':
	main()
