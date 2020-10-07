//
// Created by 薛智钧 on 2020/3/17.
//

#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 // Given a linked list, remove the n-th node from the end of list and return its head.
 // Given n will always be valid.

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(-1), *cur = dummy;
        dummy->next = head;
        int l = 0; // 保存链表长度
        while (cur->next){
            cur = cur->next;
            ++l;
        }
        int index = l - n; // 倒数第n个节点的位置
        cur = dummy;
        for (int i = 0; i < index; ++i){ // 找到目标节点的前驱
            cur = cur->next;
        }
        cur->next = (cur->next)->next;
        return dummy->next;
    }
};

