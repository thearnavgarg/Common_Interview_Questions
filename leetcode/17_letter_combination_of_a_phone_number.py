class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        ###############################
        # Helper functions
        
        def create_combinations(combinations, text_list):
            new_combination = []
            for combination in combinations:
                for text in text_list:
                    new_combination.append(combination + text)
            return new_combination
        
    
        ###############################
        
        if not digits:
            return []
        
        number2text = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        
        print(int(digits[0]))
        combinations = number2text[int(digits[0])]
        
        for i in range(1, len(digits)):
            digit = int(digits[i])
            text_list = number2text[digit]
            combinations = create_combinations(combinations, text_list)
        
        return combinations
