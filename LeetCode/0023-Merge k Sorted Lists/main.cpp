//
// Created by 薛智钧 on 2020/4/9.
//
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode* next;
    explicit ListNode(int x): val(x), next(nullptr) { }
};

/*
 *  Merge k sorted linked lists and return it as one sorted list.
 *  Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
 * */

class Solution {
    // 利用divide and conquer的方法
    // 思路：例如 n = 6, 可以首先1和4，2和5，3和6合并
    // 然后继续迭代，下一步只需要合并3个列表即可，直到剩下最后一个列表返回
    // 即为结果
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;
        int n = (int)lists.size();
        while (n > 1){
            int k = (n + 1) / 2;
            for (int i = 0; i < n / 2; ++i){
                lists[i] = mergeTowLists(lists[i], lists[i + k]);
            }
            n = k; // n等于合并后剩下的lists数目
        }
        return lists[0];
    }

    static ListNode* mergeTowLists(ListNode* l1, ListNode* l2){
        if (!l1) return l2;
        if (!l2) return l1;

        ListNode* head = (l1->val < l2->val) ? l1 : l2;
        ListNode* notHead = (l1->val < l2->val) ? l2 : l1;
        head->next = mergeTowLists(head->next, notHead);
        return head;
    }

    ListNode* mergeKLists_2(vector<ListNode*>& lists){
        int k = (int)lists.size();
        ListNode* dummy = new ListNode(-1), *cur = dummy;
        while (true){
            ListNode* minNode = nullptr;
            int minPointer = -1; // 记录minNode在lists中的位置
            for (int i = 0; i < k; ++i){ // 依次遍历所有list
                if(!lists[i]) continue;
                if (!minNode || lists[i]->val < minNode->val){
                    minNode = lists[i];
                    minPointer = i;
                }
            }
            if (minPointer == -1) break; // lists中的所有list遍历结束
            cur->next = minNode;
            cur = cur->next;
            lists[minPointer] = lists[minPointer]->next;
        }
        return dummy->next;
    }


    /*
     * priority_queue<>默认是大根堆的，这是因为优先队列队首指向最后，队尾指向最前面的缘故！每次入队元素进去经排序调整后，
     * 优先级最大的元素排在最前面，也就是队尾指向的位置，这时候队首指向优先级最小的元素！
     * 所以虽然使用less但其实相当于greater，我们重载运算符的时候比较函数里面写>就相当于<排序方式
     * */

    // 小顶堆回调函数
    struct cmp{
        bool operator()(ListNode* a, ListNode* b){
            return a->val > b->val;
        }
    };

    ListNode* mergeKLists_3(vector<ListNode*>& lists){
        // 构建小顶堆
        priority_queue<ListNode*, vector<ListNode*>, cmp> pq;
        for (auto node : lists){
            if (node) pq.push(node);
        }

        ListNode* dummy = new ListNode(-1), *cur = dummy;
        while (!pq.empty()){
            ListNode* minNode = pq.top(); pq.pop(); // 弹出最小节点
            cur->next = minNode; cur = cur->next;
            if (minNode->next) pq.push(minNode->next); // 最小节点的下一节点如队
        }
        return dummy->next;
    }
};