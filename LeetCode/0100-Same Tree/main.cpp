//
// Created by 薛智钧 on 2020/3/26.
//

#include <vector>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

/*
 * Given two binary trees, write a function to check if they are the same or not.

   Two binary trees are considered the same if they are structurally identical
   and the nodes have the same value.
 * */

class Solution {
public:
    // 利用preorder traversal 判断是否是same tree
    bool isSameTree_1(TreeNode* p, TreeNode* q) {
        stack<TreeNode*> tmp_p{{p}};
        stack<TreeNode*> tmp_q{{q}};
        while (!tmp_p.empty() && !tmp_q.empty()){
            p = tmp_p.top(); tmp_p.pop();
            q = tmp_q.top(); tmp_q.pop();
            if (!p && !q) continue;
            if ((p && !q) || (!p && q) || (p->val != q->val)) return false;
            tmp_p.push(p->right); tmp_p.push(p->left);
            tmp_q.push(q->right); tmp_q.push(q->left);
        }
        return true;
    }

    // 利用inorder traversal 判断是否是same tree
    bool isSameTree_2(TreeNode* p, TreeNode* q){
        stack<TreeNode*> p_tmp;
        stack<TreeNode*> q_tmp;
        while (true){
            while (p || q){ // 只要p或q不为null，就向左子树遍历
                if ((p && !q) || (!p && q) || (p->val != q->val)) return false;
                p_tmp.push(p); q_tmp.push(q);
                p = p->left; q = q->left;
            }
            // 当且仅当p,q皆为空，且p_tmp和q_tmp也都为空时，返回true
            if (p_tmp.empty() && q_tmp.empty()) return true;
            p = p_tmp.top(); p_tmp.pop();
            q = q_tmp.top(); q_tmp.pop();
            p = p->right; q = q->right;
        }
    }

};