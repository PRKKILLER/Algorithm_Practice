//
// Created by 薛智钧 on 2020/4/8.
//
#include <iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode* next;
    explicit ListNode(int x): val(x), next(nullptr) {}
};

/*
 * Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
 * */

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode(-1), *pre = dummy;
        pre->next = head;
        ListNode* cur = head;
        while(cur){
            if (cur->val == val)
                pre->next = cur->next;
            else
                pre = cur;
            cur = cur->next;
        }
        return dummy->next;
    }
};

