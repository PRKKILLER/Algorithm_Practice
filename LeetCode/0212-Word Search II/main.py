"""  
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.


Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_END = '$'
        
        # build the trie
        trie = {}
        
        for word in words:
            node = trie
            for c in word:
                if not c in node:
                    node[c] = {}
                node = node[c]
            node[WORD_END] = word
        
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        match_words = []
        
        def backtrack(i, j, parentNode):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if not board[i][j] in parentNode:
                return
            
            letter = board[i][j]
            curNode = parentNode[letter]
            
            if WORD_END in curNode:
                match_words.append(curNode[WORD_END])
            
            board[i][j] = '#'
            
            for x, y in directions:
                di, dj = i + x, j + y
                backtrack(di, dj, curNode)
            
            board[i][j] = letter



        for i in range(m):
            for j in range(n):
                backtrack(i, j, trie)
        
        return list(set(match_words))