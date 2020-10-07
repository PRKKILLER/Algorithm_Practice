//
// Created by 薛智钧 on 2020/3/27.
//

#include <vector>
#include <stack>
#include <queue>
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

/*
 * Invert a binary tree.

  Example:

  Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 * */

class Solution {
public:
    // 解法1：递归
    TreeNode* invertTree_r1(TreeNode* root) {
        if (!root) return nullptr;
        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp;
        invertTree_r1(root->left);
        invertTree_r1(root->right);
        return root;
    }

    TreeNode* invertTree_r2(TreeNode* root){
        if (!root) return nullptr;
        TreeNode* tmp = root->left; // 保存原本的左孩子
        root->left = invertTree_r2(root->right);
        root->right = invertTree_r2(tmp);
        return root;
    }

    TreeNode* invertTree_I1(TreeNode* root){
        if (!root) return nullptr;
        queue<TreeNode*> q{{root}};
        while (!q.empty()){
            TreeNode* node = q.front(); q.pop();
            TreeNode* tmp = node->left;
            node->left = node->right;
            node->right = tmp;
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        return root;
    }
};



