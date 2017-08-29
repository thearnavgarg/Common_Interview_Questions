'''
Find the least number of substitutions, insertions, and deletions required to get from one string to another.

Ex: Consider transforming the string “alien” into the string “sales.” We can begin by inserting an “s” at the front 
of “alien” to make “salien”. Then we delete the “i” to make “salen.” Then we replace the “n” with an “s” to make 
“sales.” That took three operations, and indeed it is not possible to transform “alien” to “sales” with fewer than three operations.
'''

def least_ops(s1, s2):
	if s1 == '':
		return len(s2)
	if s2 == '':
		return len(s1) 
	if s1[0] == s2[0]:
		return least_ops(s1[1:], s2[1:])
	sub_ops = 1 + least_ops(s1[1:], s2[1:])
	del_ops = 1 + least_ops(s1[1:], s2)
	ins_ops = 1 + least_ops(s1, s2[1:])
	return min(sub_ops, del_ops, ins_ops)
