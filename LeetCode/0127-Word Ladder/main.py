"""  
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
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
"""

"""  
此题是标准的 BFS 框架，但是难点在于寻找当前 word 的 Neighborhood
"""
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList: return 0
        
        visited = set()
        ladder = 1
        l = len(beginWord)
        q = deque([beginWord])
        
        while q:
            sz = len(q)
            for i in range(sz):
                cur_word = q.popleft()
                if cur_word == endWord:
                    return ladder
                
                # check if the cur_word's neighbor in the wordList
                for j in range(l):
                    for c in 'abcdefghijklmnopqrstuvwxyz': # 关键
                        next_word = cur_word[:j] + c + cur_word[j+1:]
                        if next_word in wordList and next_word not in visited:
                            q.append(next_word)
                            visited.add(next_word)
            ladder += 1
        
        return 0                           