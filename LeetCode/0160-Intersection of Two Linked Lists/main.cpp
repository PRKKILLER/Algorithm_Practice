//
// Created by 薛智钧 on 2020/4/8.
//
#include <iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode* next;
    explicit ListNode(int x): val(x), next(nullptr) { }
};

/*
 * Write a program to find the node at which the intersection of two singly linked lists begins.
 * */

class Solution {
public:
    // 思路：获得两个列表的长度，然后让长的列表的指针先走
    // 之后两个指针一起运动
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* curA = headA, *curB = headB;
        int lenA = 0, lenB = 0;
        while (curA){
            ++lenA;
            curA = curA->next;
        }
        while (curB){
            ++lenB;
            curB = curB->next;
        }
        curA = headA, curB = headB;

        if (lenA >= lenB){
            int diff = lenA - lenB;
            while(diff--)
                curA = curA->next;
        }else{
            int diff = lenB - lenA;
            while(diff--)
                curB = curB->next;
        }
        // 当两个指针不相同时再一起运动
        while (curA != curB){
            curA = curA->next;
            curB = curB->next;
        }
        return curA;
    }
};

