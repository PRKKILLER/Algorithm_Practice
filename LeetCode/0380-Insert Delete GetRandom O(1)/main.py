"""  
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. 
Returns true if the item was not present, false otherwise.

bool remove(int val) Removes an item val from the set if present. 
Returns true if the item was present, false otherwise.

int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

"""  
The idea is to use hashmap + list
use hashmap to track the given number's index, to help achieve O(1) deletion time
"""




from random import choice
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.mp:
            return False

        self.arr.append(val)
        self.mp[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.mp:
            return False

        # move need to delete value to the end of the array, this can achieve O(1) deletion time
        idx, last_num = self.mp[val], self.arr[-1]
        self.arr[idx], self.mp[last_num] = last_num, idx
        self.arr.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.arr)
