"""  
Given two words (beginWord and endWord), and a dictionary's word list, 
find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.

- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.


Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
"""

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict
        
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
        # key: current word
        # value: all path get to the currentWord
        layer = {beginWord: [[beginWord]]}
        n = len(beginWord)
        
        while layer:
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                
                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in word_set:
                            # 不同的 word 可能会得到相同的 new_word, 但是path不相同
                            new_layer[new_word] += [path + [new_word] for path in layer[word]]
            
            word_set -= set(new_layer.keys())
            layer = new_layer # move down to the new_layer
        
        return []