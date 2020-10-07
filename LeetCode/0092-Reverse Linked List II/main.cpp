//
// Created by 薛智钧 on 2020/3/19.
//
#include <iostream>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Reverse a linked list from position m to n. Do it in one-pass.
// Note: 1 ≤ m ≤ n ≤ length of list.

// Example:
// Input: 1->2->3->4->5->NULL, m = 2, n = 4
// Output: 1->4->3->2->5->NULL

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (!head || m == n) return head;
        ListNode* dummy = new ListNode(-1), *cur = dummy;
        dummy->next = head;
        // cur 指向m的前一个节点
        for (int i = 0; i < m - 1; ++i) cur = cur->next;
        // [m,n]之间的节点倒插入节点cur之后
        ListNode* s1 = cur->next;
        for (int j = 0; j < n - m; ++j){
            ListNode* tmp = s1->next;
            s1->next = tmp->next;
            tmp->next = cur->next;
            cur->next = tmp;
        }
        return dummy->next;
    }


    static void deleteNode_notwork(ListNode* node) {
        ListNode* post = node->next;
        while (post) {
            node->val = post->val;
            node = post;
            post = post->next;
        }
//        node = nullptr; 注意，这样做没有用，因为这只是pass pointer by value，
//        而实际的node->pre->next并没有改变
    }

    static void deleteNode(ListNode* node) {
        node->val = node->next->val;
        ListNode* tmp = node->next;
        node->next = tmp->next;
        delete tmp;
    }
};

int main() {
    int a[4] = {4,5,1,9};
    ListNode* dummy = new ListNode(-1), *cur = dummy;
    for (int i : a) {
        cur->next = new ListNode(i);
        cur = cur->next;
    }
    ListNode* head = dummy->next, *target = head->next;
    Solution::deleteNode(target);
    while (head) {
        cout << head->val << "->";
        head = head->next;
    }
}

