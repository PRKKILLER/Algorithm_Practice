//
// Created by 薛智钧 on 2020/3/18.
//

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Reverse a singly linked list.

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr, *cur = head;
        while (cur){
            ListNode* temp = cur->next; // 暂存cur的下一个节点
            cur->next = prev;
            prev = cur;
            cur = temp;
        }
        head = prev;
        return head;
    }

    // 递归解法
    ListNode* reverseList_recursive(ListNode* head){
        if (!head || !(head->next)) return head;
        ListNode* last = reverseList_recursive(head->next); // 递归后会指向最后一个节点
        head->next->next = head;
        head->next = nullptr;
        return last;
    }
};


