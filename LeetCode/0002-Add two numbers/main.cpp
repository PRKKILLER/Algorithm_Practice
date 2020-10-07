//
// Created by 薛智钧 on 2020/3/16.
//
#include <iostream>

/*
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order and each of their nodes contain a single digit.
 * Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 */

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    explicit ListNode(int x) : val(x), next(nullptr) {}
};

// 思路: 两个列表都逆序存储数字，且输出列表也可为逆序数字，
// 因此低位在前，高位在后，可以对应数位可以直接相加
// 用carry 保存数字的进位
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // dummy为新建列表的头结点
        ListNode* dummy = new ListNode(-1), *cur = dummy;
        int carry = 0;  // 保存进位

        while(l1 || l2){
            int val1 = l1 ? l1->val : 0;
            int val2 = l2 ? l2->val : 0;
            int sum = val1 + val2 + carry;
            carry = sum / 10;
            cur->next = new ListNode(sum % 10);
            cur = cur->next;
            if (l1)  l1 = l1->next;
            if (l2) l2 = l2->next;
        }
        if (carry != 0 ) cur->next = new ListNode(1);
        return dummy->next;
    }

    /*---------递归解法--------*/
    ListNode* adder(ListNode* l1, ListNode* l2, int carry){
        int curVal = 0; // 保存当前位数值
        if (l1){
            curVal += l1->val;
            l1 = l1->next;
        }
        if (l2){
            curVal += l2->val;
            l2 = l2->next;
        }
        curVal += carry;
        carry = curVal / 10;

        ListNode* head = new ListNode(curVal % 10);
        if (l1 || l2 || carry)
            head->next = adder(l1, l2, carry);
        return head;
    }

    ListNode* addTwoNumbers_2(ListNode* l1, ListNode* l2){
        return adder(l1, l2, 0);
    }
};
