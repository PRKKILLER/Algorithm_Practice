"""  
Implement a product recommendation system
System has following 2 functions: add(), suggest()

use add() to add words into the system
use suggest(prefix) to recommend product

For example: 
add: 'app', 'apple', 'animal'
suggest('app'): -> ['app', 'apple']
"""

from typing import List

# using hash table to implement trie
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    # time complexity: O(m), where m is the length of the words
    # space complexity: O(m)
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node['#'] = '#' # mark this is the end of the inserted words

    # time complexity: O(m), where m is the length of the words
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie
        for w in word:
            if w not in node:
                return False
            node = node[w]
        return '#' in node # check if word is inserted or just a prefix

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie
        for w in prefix:
            if w not in node:
                return False
            node = node[w]
            
        return True

    def wordSuggestion(self, prefix: str) -> List[str]:
        """
        Return all words inserted in the trie that has the prefix
        """
        node = self.trie
        for w in prefix:
            if w not in node:
                return []
            node = node[w]
        
        res = []
        self.dfs(prefix, res, node)
        return res

    def dfs(self, prefix: str, res: List[str], node):
        if '#' in node:
            res.append(prefix)

        for item in node:
            if item == '#':
                continue
            else:
                self.dfs(prefix + item, res, node[item])