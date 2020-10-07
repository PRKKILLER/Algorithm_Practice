//
// Created by 薛智钧 on 2020/3/18.
//
#include <unordered_map>
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Given a sorted linked list, delete all nodes that have duplicate numbers,
// leaving only distinct numbers from the original list.
// Return the linked list sorted as well.

class Solution {
public:

    // 思路1：利用hashmap, 记录每种元素出现的次数
    // 删去出现次数 > 1的元素; 需要遍历两次，时间、空间复杂度都较大
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return nullptr;
        ListNode* dummy = new ListNode(-1);
        ListNode* s1 = dummy, *s2 = head;
        unordered_map<int, int> dict; // dict[key] 默认值为0
        while (s2){
            dict[s2->val] += 1;
            s2 = s2->next;
        }
        s2 = head;
        while (s2){
            if (dict[s2->val] < 2){
                s1->next = s2;
                s1 = s1->next;
            }
            s2 = s2->next;
        }
        s1->next = nullptr;
        return dummy->next;
    }


    ListNode* deleteDuplicates_2(ListNode* head){
        if (!head || !(head->next)) return head;
        ListNode* dummy = new ListNode(-1), *s1 = dummy;
        s1->next = head; // s1初始指向head
        while (s1->next){
            ListNode* s2 = s1->next; // 每次while循环之前，s2总是指向s1的下一个位置
            while (s2->next && s2->val == (s2->next)->val)
                s2 = s2->next;
            // 判断当前s2和s2初始位置是否是同一个，若不是，则表明进入过while循环
            // s1应指向s2的下一个位置
            if (s2 != s1->next) s1->next = s2->next;
            else s1 = s1->next;
        }
        return dummy->next;
    }
};

int main(){
    std::unordered_map<int, int> m;
    m[0] += 1;
    std::cout << m[0];
}