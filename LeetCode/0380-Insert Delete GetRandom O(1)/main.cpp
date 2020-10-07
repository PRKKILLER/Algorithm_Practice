//
// Created by 薛智钧 on 2020/6/12.
//
#include <unordered_map>
#include <iostream>
using namespace std;
/*
 *  Design a data structure that supports all following operations in average O(1) time.


  insert(val): Inserts an item val to the set if not already present.
  remove(val): Removes an item val from the set if present.
  getRandom: Returns a random element from current set of elements.
  Each element must have the same probability of being returned.
 * */

class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() = default;

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (m[val]) return false;
        m[val] = 1;
        return true;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (!m[val]) return false;
        m.erase(val);
        return true;
    }

    /** Get a random element from the set. */
    int getRandom() {
        int rnd_index = random() % m.size();
        auto item = m.begin();
        auto res = next(item, rnd_index);
        return (int)res;
    }

private:
    unordered_map<int, int> m;
};
