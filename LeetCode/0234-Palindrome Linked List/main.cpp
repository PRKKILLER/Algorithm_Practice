//
// Created by 薛智钧 on 2020/3/18.
//
#include <stack>
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};


// Given a singly linked list, determine if it is a palindrome.
// Follow up: Could you do it in O(n) time and O(1) space?
class Solution {
public:

    // 思路：利用stack的先进后出的性质将链表逆序，之后逐个比较
    // 因为只要前半个链表和后半个链表对应值相等，就是一个回文链表，
    // 而并不需要再比较一遍后半个链表，所以我们可以找到链表的中点
    bool isPalindrome(ListNode* head) {
        if (!head || !(head->next)) return true;
        stack<int> dict;
        ListNode* cur = head;
        while(cur){
            dict.push(cur->val);
            cur = cur->next;
        }
        cur = head;
        // stack.size()是动态变化的，每次stack.pop()/ stack.push()时
        // stack.size()的值都会相应改变
        // 缺点，存在越界的可能
        size_t len = dict.size();
        for (int i = 0; i < len / 2; ++i) {
            if (cur->val != dict.top())
                return false;
            cur = cur->next;
            dict.pop();
        }
        return true;
    }


    // 思路2，使用fast, slow指针寻找链表中点
    // 原理: fast的步长为2，slow的步长为1，当fast走到链表末尾时，slow正好走到链表的中点
    // tricky part: 要注意区分链表长度为奇数/ 偶数 的情况

    bool isPalindrome_2(ListNode* head){
        if (!head || !(head->next)) return true;
        stack<int> dict{{head->val}}; // stack初始化，预先放入链表头元素
        ListNode* slow = head, *fast = head;
        // 注意 while 循环条件
        // 以fast->next = null跳出循环的情况是链表长度为奇数
        // 以(fast->next)->next = null 跳出循环的情况是链表长度为偶数
        while (fast->next && (fast->next)->next){
            slow = slow->next;
            fast = (fast->next)->next;
        }
        if (!(fast->next)) dict.pop(); // 链表长度为奇数情况，pop()出链表中间元素
        // 比较链表前半段元素和后半段元素
        while (slow->next){
            slow = slow->next;
            if (slow->val != dict.top())
                break;
            dict.pop();
        }
        return true;
    }

    // 思路3：利用快慢指针找到链表中点，对链表后半段逆序操作
    // 此时空间复杂度为O(1)
    bool isPalindrom_3(ListNode* head){
        if (!head || !(head->next)) return true;
        ListNode* slow = head, *fast = head;
        while(fast->next && (fast->next)->next){
            slow = slow->next;
            fast = (fast->next)->next;
        }
        // 对后半链表进行逆序
        ListNode* head_last = slow->next, *prev = nullptr;
        while (head_last){
            ListNode* temp = head_last->next;
            head_last->next = prev;
            prev = head_last;
            head_last = temp;
        }
        head_last = prev; // 后半链表逆序之后的头结点
        slow = head;
        while (head_last){
            if (head_last->val != slow->val)
                return false;
            slow = slow->next;
            head_last = head_last->next;
        }
        return true;
    }
};

int main(){
    ListNode*head = new ListNode(1);
    ListNode* cur = head;
    int a[] = {1,2,1};
    for (int i : a){
        cur->next = new ListNode(i);
        cur = cur->next;
    }
    Solution sol;
    cout << sol.isPalindrome(head);
}

