//
// Created by 薛智钧 on 2020/6/5.
//

struct ListNode {
    int val;
    ListNode* next;
    explicit ListNode(int x): val(x), next(nullptr) {}
};

/*
 * Write a function to delete a node (except the tail) in a singly linked list,
 * given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:
 * */

// 思路：因为题目只给定了当前节点的入口，因此无法得到其前驱节点，
// 并且给定节点不会是tail，因此可以将current node的后一个node的val赋值给current node,
// 然后delete 后一个node

class Solution {
public:
    // 思路：因为无法得知当前节点的前驱，并且当前node不是tail，因此只能将当前node的后面节点的值依次前移，
    // 然后删除最后一个node，才能达到题意
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        ListNode* tmp = node->next;
        node->next = tmp->next;
        delete tmp;
    }
};
