//
// Created by 薛智钧 on 2020/5/28.
//
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

/*
 *  Design and implement a data structure for Least Recently Used (LRU) cache.
 *  It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
 otherwise return -1.
 
put(key, value) - Set or insert the value if the key is not already present.
 When the cache reached its capacity, it should invalidate the least recently used item
 before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

2 stands for capacity
LRUCache cache = new LRUCache( 2 );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
 * */

class LRUCache {
public:
    explicit LRUCache(int capacity): _capacity(capacity) {}

    int get(int key) {
        if (m.count(key)) {
            Node* node = m[key];
            // 将访问的node插入头部
            remove(node);
            setHead(node);
            cout << "get: " << key << ":" << node->value << endl;
            return node->value;
        }
        cout << "get: None" << endl;
        return -1;
    }

    void put(int key, int value) {
        if (m.count(key)) {
            Node* old = m[key];
            old->value = value;
            remove(old);
            setHead(old);
        } else {
            Node* newNode = new Node(key, value);
            if (m.size() == _capacity) { // 达到cache容量
                m.erase(tail->key); // 删除list中最后一个key
                remove(tail);
                setHead(newNode);
            } else {
                setHead(newNode);
            }
            m[key] = newNode;
        }
        cout << "put: " << key << ":" << value << endl;
    }

private:
    struct Node {
        int key;
        int value;
        Node* pre;
        Node* next;
        Node (int k, int val) : key(k), value(val), pre(nullptr), next(nullptr) {}
    };
    int _capacity;
    Node* head = nullptr, *tail = nullptr;
    unordered_map<int, Node*> m;

    // 将node从Bi-Linked List中移除
    void remove(Node* node) {
        node->pre ? node->pre->next = node->next : head = node->next;
        node->next ? node->next->pre = node->pre : tail = node->pre;
    }

    // 将node加入到Bi-Linked List
    void setHead(Node* node) {
        node->next = head;
        node->pre = nullptr;
        if (head) head->pre = node;
        head = node;
        if (!tail) tail = head;
    }
};

int main() {
    LRUCache lru(2);
    lru.put(1, 100);
    lru.put(2, 200);
    lru.get(1);
    lru.get(3);
    lru.put(3, 100);
    lru.get(2);
}