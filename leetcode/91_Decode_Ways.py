
# CHEATED: Looked into the discussion to come up with this peice of shit but beautiful solution. 
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        226 = nw(2) +
        '''
        if not s:
            return 0

        table = [0]*(len(s)+1)
        table[0] = 1
        table[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s)+1):
            singleDigit = int(s[i-1:i])
            doubleDigit = int(s[i-2:i])
            if singleDigit > 0:
                table[i] += table[i-1]
            if doubleDigit >= 10 and doubleDigit <= 26:
                table[i] += table[i-2]
        return table[-1]


'''

Initially tried this but it didn't work because of shitty test cases like "01"... 

class Solution:
    def numDecodings(self, s: str) -> int:
        def decoder(s):
            num = 1
            if not s:
                return 0
            if len(s) <= 2 and int(s[:2]) <= 26 and int(s[:2]) >= 10:
                num += 1
            if len(s) <= 1:
                num += 1
            num += decoder(s[2:])
            return num
        
        return decoder(s)

'''
