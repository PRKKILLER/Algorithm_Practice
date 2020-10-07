//
// Created by 薛智钧 on 2020/3/27.
//

#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Given a binary tree,
// return the level order traversal of its nodes' values.
// (ie, from left to right, level by level).

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (!root) return {};
        vector<vector<int>> level_order; // 保存层次遍历
        queue<TreeNode*> tmp{{root}}; // 辅助队列
        while (!tmp.empty()){
            vector<int> one_level;
            // 辅助队列的大小会随着队列的改变而改变
            // 因此不能将queue.size()放到循环的条件里
            // 但是可以放到初始化条件里
            int curr_len = (int)tmp.size(); // 记录当前队列长度，即当前层的节点数
            for (int i = curr_len; i > 0; --i) {
                TreeNode* p = tmp.front(); tmp.pop();
                one_level.push_back(p->val);
                if (p->left) tmp.push(p->left); // 左孩子先进先出
                if (p->right) tmp.push(p->right); // 右孩子后进后出
            }
            level_order.push_back(one_level);
        }
        return level_order;
    }
};