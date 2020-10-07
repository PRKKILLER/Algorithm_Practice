//
// Created by 薛智钧 on 2020/3/22.
//
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

/*
 * Given a linked list, rotate the list to the right by k places, where k is non-negative.

   Example 1:

   Input: 1->2->3->4->5->NULL, k = 2
   Output: 4->5->1->2->3->NULL
   Explanation:
   rotate 1 steps to the right: 5->1->2->3->4->NULL
   rotate 2 steps to the right: 4->5->1->2->3->NULL
 * */

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (k == 0 || !head || !head->next) return head;
        int len = 0; // 链表的长度
        ListNode* cur = head, *last = nullptr;
        while(cur) {
            ++ len;
            cur = cur->next;
        }
        k = k % len; // 归一化k
        if (k == 0)return head;

        cur = head;
        for (int i = 0; i < len - k - 1; ++i) {
            cur = cur->next;
        }
        last = cur->next;
        cur->next = nullptr;
        cur = head;
        head = last;
        while (last->next){
            last = last->next;
        }
        last->next = cur; // 将前半部分链表接到后半部分的后面
        return head;
    }

    // 解法2: 遍历整个链表，得到链表的长度n，然后此时将链表的头尾连接
    // 然后再从头出发，向后走 n - k % n 个节点到达新链表头结点的前一个节点，然后再断开链表即可
    ListNode* rotateRight_2(ListNode* head, int k){
        if (k == 0 || !head || !head->next) return head;
        int len = 1;
        ListNode* cur = head;
        while (cur->next){
            ++len;
            cur = cur->next;
        }
        cur->next = head; // 链表头尾相连
        k %= len; // 归一化k
        for (int i = 0; i < len - k; ++i) {
            cur = cur->next;
        }
        head = cur->next;
        cur->next = nullptr; // 断开链表
        return head;
    }


};

int main(){
    int a[] = {1,2};
    ListNode* dummy = new ListNode(-1), *cur = dummy;
    for (int i : a){
        cur->next = new ListNode(i);
        cur = cur->next;
    }
    ListNode* head = dummy->next;
    Solution sol;
    head = sol.rotateRight_2(head, 2);
    while (head){
        cout << head->val << ",";
        head = head->next;
    }
}