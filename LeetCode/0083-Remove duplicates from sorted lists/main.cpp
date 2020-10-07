//
// Created by 薛智钧 on 2020/3/18.
//

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Given a sorted linked list, delete all duplicates such that each element appear only once.

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return nullptr;
        ListNode* s1 = head, *s2 = head->next;
        while (s2){
            if (s2->val != s1->val){
                s1->next = s2;
                s1 = s1->next;
            }
            s2 = s2->next;
        }
        s1->next = nullptr;  // 此时s1指向非重复链表末尾，s1->next应为NULL
        return head;
    }
};

