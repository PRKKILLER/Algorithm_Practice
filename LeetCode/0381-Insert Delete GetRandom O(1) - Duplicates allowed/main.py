"""  
Implement the RandomizedCollection class:

RandomizedCollection() Initializes the RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset if not present. 
Returns true if the item was not present, false otherwise.

bool remove(int val) Removes an item val from the multiset if present. 
Returns true if the item was present, false otherwise. 
Note that if val has multiple occurrences in the multiset, we only remove one of them.

int getRandom() Returns a random element from the current multiset of elements 
(it's guaranteed that at least one element exists when this method is called). 
The probability of each element being returned is 
linearly related to the number of same values the multiset contains.


You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

"""  
该题和380解法基本相似，难点在于存在duplicate的时候，以 O(1) 的时间复杂度完成 delete
做法在于使用 hashmap, key: val; value: set() which contains indexes corresponding to the value 
"""




from random import choice
from collections import defaultdict
class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dic = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.dic[val].add(len(self.arr))
        self.arr.append(val)
        return len(self.dic[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """

        # if val don't have its corresponding index
        # note: we cannot use "if val not in self.dic",
        # since this is a defaultdict, and we didn't delete key
        if not self.dic[val]:
            return False

        idx, last_num = self.dic[val].pop(), self.arr[-1]
        self.arr[idx] = last_num
        self.dic[last_num].add(idx)
        self.dic[last_num].remove(len(self.arr) - 1)
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.arr)
