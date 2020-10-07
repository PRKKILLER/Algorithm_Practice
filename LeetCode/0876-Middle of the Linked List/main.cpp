//
// Created by 薛智钧 on 2020/3/19.
//

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Given a non-empty, singly linked list with head node head, return a middle node of linked list.
// If there are two middle nodes, return the second middle node.

class Solution {
public:

    // 思路：利用快慢指针
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head, *fast = head;
        while (fast->next && (fast->next)->next){
            slow = slow->next;
            fast = (fast->next)->next;
        }
        if (fast->next && !(fast->next)->next) // 长度为偶数的情况
            slow = slow->next; // 返回第二个middle节点
        return slow;
    }

    // 等价方法;  好处：不用进行长度的奇偶判断
    ListNode* middleNode_2(ListNode* head){
        ListNode* slow = head, *fast = head;
        while (fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};


