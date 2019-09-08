class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def getValueFromChar(s, idx):
            return 1 if s[idx] == '1' else 0
        
        # come back and handle edge cases. 
        if not a and not b:
            return ''
        
        if not a or not b:
            return a if not b else b
        
        result = ''
        carryOver = 0
        aIndex = len(a)-1
        bIndex = len(b)-1
        
        while aIndex >= 0 or bIndex >= 0:
            aValue = 0
            bValue = 0
            if aIndex >= 0:
                aValue = getValueFromChar(a, aIndex)
            if bIndex >= 0:
                bValue = getValueFromChar(b, bIndex)
            
            rValue = (aValue + bValue + carryOver) % 2
            carryOver = (aValue + bValue + carryOver) // 2
            result = str(rValue) + result
            aIndex -= 1
            bIndex -= 1
        
        if carryOver == 1:
            result = str(carryOver) + result
        
        return result
