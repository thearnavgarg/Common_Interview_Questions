"""
There is a parking lot with only one empty spot. Given the initial state
of the parking lot and the final state. Each step we are only allowed to
move a car
out of its place and move it into the empty spot.
The goal is to find out the least movement needed to rearrange
the parking lot from the initial state to the final state.

Say the initial state is an array:

[1, 2, 3, 0, 4],
where 1, 2, 3, 4 are different cars, and 0 is the empty spot.

And the final state is

[0, 3, 2, 1, 4].
We can swap 1 with 0 in the initial array to get [0, 2, 3, 1, 4] and so on.
Each step swap with 0 only.

Edit:
Now also prints the sequence of changes in states.
Output of this example :-

initial: [1, 2, 3, 0, 4]
final:   [0, 3, 2, 1, 4]
Steps =  4
Sequence : 
0 2 3 1 4
2 0 3 1 4
2 3 0 1 4
0 3 2 1 4
"""

'''
rough
-----

[1, 2, 3, 0, 4]
[0, 3, 2, 1, 4]

[0, 2, 3, 1, 4]
[0, 3, 2, 1, 4]

'''

def garage(start, final):
    if len(start) != len(final):
        return None
    if not start and not final:
        return start
    moves = 0
    start_zero, end_zero = 0, 0
    for i, (s, e) in enumerate(zip(start, final)):
        if s == 0:
            start_zero = i
        if e == 0:
            end_zero = i
    if start_zero != end_zero:
        start[end_zero], start[start_zero] = start[start_zero], start[end_zero]
        moves += 1
    swaps = 0
    for i, (s, e) in enumerate(zip(start, final)):
        if s != e:
            swaps += 1
    return moves + (swaps//2)*3

start = [1, 2, 3, 0, 4]
final = [0, 3, 2, 1, 4]
print(garage(start, final))




