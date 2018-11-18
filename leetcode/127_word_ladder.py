'''
Given two words (beginWord and endWord), and a dictionary's word list,
 find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.'''

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """

    def helper(wordList, path, result, graph, start, end, visited):
        if start == end:
            result.append(path[:])
        if start in visited:
            return
        visited.add(start)
        for word in graph[start]:
            path.append(word)
            helper(wordList, path, result, graph, word, end, visited)
            path.pop()

    def one_transformation(word1, word2):
        counter = 0
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                counter += 1
        if counter == 1:
            return True
        return False

    from collections import defaultdict
    graph = defaultdict(list)
    if endWord not in wordList:
        return None
    wordList.append(beginWord)
    for i in range(0, len(wordList)):
        for j in range(0, len(wordList)):
            word1, word2 = wordList[i], wordList[j]
            if word1 != word2 and one_transformation(word1, word2):
                graph[word1].append(word2)
    
    path, result = [beginWord], []
    visited = set()
    helper(wordList, path, result, graph, beginWord, endWord, visited)
    return result

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))



