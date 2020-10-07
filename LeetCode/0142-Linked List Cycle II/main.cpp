//
// Created by 薛智钧 on 2020/3/17.
//

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Given a linked list, return the node where the cycle begins.
// If there is no cycle, return null.
//
// To represent a cycle in the given linked list,
// we use an integer pos which represents the position (0-indexed) in the linked list
// where tail connects to. If pos is -1, then there is no cycle in the linked list.
//
// Note: Do not modify the linked list.

class Solution {
public:
    // 思路：快、慢指针
    // 难点：快、慢指针第一次相遇的位置不一定是链表中环的起始位置
    // 设: 进入环前的路程为a，当快、慢指针相遇时，快指针走过的路程是慢指针的2倍
    // 设慢指针相遇时走过路程为x, 则慢指针在圈内的位置相对于圈的起点是 (x-a)
    // 圈剩下的距离: x-(x-a) = a
    // 此时让慢指针回到head,快指针在原来位置，此时两个指针都stripe = 1运动，则相遇点即为环形的起点
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head, *fast = head;
        while (fast && fast->next){
            slow = slow->next;
            fast = (fast->next)->next;
            if (slow == fast) break;
        }
        if (!fast || !(fast->next)) return nullptr;
        slow = head;
        while (slow != fast){
            slow = slow->next;
            fast = fast->next;
        }
        return slow;
    }
};

