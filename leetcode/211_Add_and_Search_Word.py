class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordCountToWordSet = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if len(word) not in self.wordCountToWordSet:
            self.wordCountToWordSet[len(word)] = set()
        self.wordCountToWordSet[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) not in self.wordCountToWordSet:
            return False
        
        def getNumMissing(word):
            missing = 0
            for char in word:
                if char == '.':
                    missing += 1
            return missing
        
        def checkWordMatch(word, wordSet):
            for storedWord in wordSet:
                foundWord = True
                for char, storedChar in zip(word, storedWord):
                    if char == '.':
                        continue
                    elif char != storedChar:
                        foundWord = False
                if foundWord:
                    return True
            return False
                
        
        missing = getNumMissing(word)
        wordSet = self.wordCountToWordSet[len(word)]
        
        if missing == len(word):
            return True
        
        # print(missing, wordSet, word)
        
        if missing == 0:
            return word in wordSet
        
        return checkWordMatch(word, wordSet)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
