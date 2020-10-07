//
// Created by 薛智钧 on 2020/3/28.
//
#include <algorithm>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};


/*
 * Given a binary tree, find its maximum depth.

 The maximum depth is the number of nodes along the longest path from
 the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
 * */

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        else return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }

    // 利用level traversal
    int maxDepth_I(TreeNode* root){
        if (!root) return 0;
        int depth = 0;
        queue<TreeNode*> q{{root}};
        while (!q.empty()){
            ++depth;
            for (size_t i = q.size(); i > 0; --i) {
                TreeNode* node = q.front(); q.pop(); // 上一层的节点出队列
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return depth;
    }
};
