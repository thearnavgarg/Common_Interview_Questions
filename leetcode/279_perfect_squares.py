class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #########################
        
        def check_perfect_square(n):
            from math import sqrt
            return int(sqrt(n))**2 == n
        
        #########################
        
        if n == 0:
            return 0
        
        if check_perfect_square(n):
            return 1
        
        table = [0 for i in range(0, n+1)]
        
        table[1] = 1
        collected_ps = [1]
        
        for i in range(2, n+1):
            min_moves = float('inf')
            if check_perfect_square(i):
                table[i] = 1
                collected_ps.append(i)
            else:
                for perfect_squares in collected_ps:
                    min_moves = min(min_moves, 1+table[i-perfect_squares])
                table[i] = min_moves
        
        return table[-1]
