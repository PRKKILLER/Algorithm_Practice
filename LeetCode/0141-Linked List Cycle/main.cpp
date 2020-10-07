//
// Created by 薛智钧 on 2020/3/17.
//

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// Given a linked list, determine if it has a cycle in it.
//
// To represent a cycle in the given linked list, we use an integer pos which represents the position
// (0-indexed) in the linked list where tail connects to.
// If pos is -1, then there is no cycle in the linked list.

class Solution {
public:
    // 思路：利用快慢、指针，若有环则一定相遇，且不会遇到null
    bool hasCycle(ListNode *head) {
        ListNode* slow = head, *fast = head;  // 快慢指针
        // 注意while循环的条件
        // 因为fast指针是每次移动2格，为了保证fast可以正确移动，
        // 要每次循环要检查当前fast位置和fast的后一个节点是否为null
        while (fast && fast->next){
            slow = slow->next;
            fast = (fast->next)->next;
            if (slow == fast) return true;
        }
        return false;
    }
};
