//
// Created by 薛智钧 on 2020/3/17.
//

#include <iostream>

/* Merge two sorted linked lists and return it as a new list.
 * The new list should be made by splicing together the nodes of the first two lists.
 * */

  struct ListNode {
          int val;
          ListNode *next;
          ListNode(int x) : val(x), next(NULL) {}
  };

class Solution {
public:
    // 思路：新建一个列表保存结果
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(-1), *cur = dummy;
        while (l1 && l2){
            // 直接利用原链表节点，不用新建节点
            if (l1->val < l2->val){
                cur->next = l1;
                l1 = l1->next;
            }else{
                cur->next = l2;
                l2 = l2->next;
                }
            cur = cur->next;
        }
        // 两个链表可能不等长，将长的列表中剩下的部分直接接到新链表的尾部
        cur->next = l1 ? l1 : l2;
        return dummy->next;
    }

    // 递归解法
    // 当某个链表为空了，就返回另一个。然后核心还是比较当前两个节点值大小，
    // 如果 l1 的小，那么对于 l1 的下一个节点和 l2 调用递归函数，将返回值赋值给 l1.next，
    // 然后返回 l1；否则就对于 l2 的下一个节点和 l1 调用递归函数，将返回值赋值给 l2.next，然后返回 l2
    ListNode* mergeTwoLists_2(ListNode* l1, ListNode* l2){
        // 递归基
        if (!l1) return l2;
        if (!l2) return l1;

        if (l1->val < l2->val){
            l1->next = mergeTwoLists_2(l1->next, l2);
            return l1;
        }else{
            l2->next = mergeTwoLists_2(l1, l2->next);
            return l2;
        }
    }

    // 递归求解
    ListNode* mergeTwoLists_3(ListNode* l1, ListNode* l2){
        if (!l1) return l2;
        if (!l2) return l1;

        ListNode* head = l1->val < l2->val ? l1 : l2;
        ListNode* notHead = l1->val < l2->val ? l2 : l1;
        head->next = mergeTwoLists_3(head->next, notHead);
        return head;
    }
};
