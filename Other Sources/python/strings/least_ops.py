'''
Find the least number of substitutions, insertions, and deletions required to get from one string to another.

Ex: Consider transforming the string “alien” into the string “sales.” We can begin by inserting an “s” at the front 
of “alien” to make “salien”. Then we delete the “i” to make “salen.” Then we replace the “n” with an “s” to make 
“sales.” That took three operations, and indeed it is not possible to transform “alien” to “sales” with fewer than three operations.

v1: Naive Recursive
Time Complexity: O(3^n)
Space Complexity: O(?)

v2: Dynamic Programming
Time Complexity: O(n*m)
Space Complexity: O(n*m)
'''

def least_ops_v1(s1, s2):
	if s1 == '':
		return len(s2)
	if s2 == '':
		return len(s1) 
	if s1[0] == s2[0]:
		return least_ops_v1(s1[1:], s2[1:])
	sub_ops = 1 + least_ops_v1(s1[1:], s2[1:])
	del_ops = 1 + least_ops_v1(s1[1:], s2)
	ins_ops = 1 + least_ops_v1(s1, s2[1:])
	return min(sub_ops, del_ops, ins_ops)

def least_ops_v2(s1, s2):
	n = len(s1)
	m = len(s2)
	dp = [[0 for i in range(m+1)] for i in range(n+1)]
	for i in range(n+1):
		for j in range(m+1):
			if i == 0:
				dp[i][j] = j 	  	
			elif j == 0:
				dp[i][j] = i 
			elif s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				sub_ops = 1 + dp[i-1][j-1]
				del_ops = 1 + dp[i-1][j]
				ins_ops = 1 + dp[i][j-1]
				dp[i][j] = min(sub_ops, del_ops, ins_ops) 	  
	return dp[n][m]

