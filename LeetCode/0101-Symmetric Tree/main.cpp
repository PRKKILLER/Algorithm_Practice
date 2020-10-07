//
// Created by 薛智钧 on 2020/3/28.
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

/**
 *
 *  Given a binary tree, check whether
 *  it is a mirror of itself (ie, symmetric around its center).
 *    1
     / \
    2   2
   / \ / \
  3  4 4  3
 *
 * **/

// 思路： 判断二叉树是否是平衡树，比如有两个节点n1, n2，
// 我们需要比较n1的左子节点的值和n2的右子节点的值是否相等，
// 同时还要比较n1的右子节点的值和n2的左子结点的值是否相等，以此类推比较完所有的左右两个节点

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        return isSymmetric(root->left, root->right);
    }

    static bool isSymmetric(TreeNode* left, TreeNode* right){
        if (!left && !right) return true;
        if ((left && !right) || (!left && right) || (left->val != right->val))
            return false;
        return (isSymmetric(left->left, right->right) && isSymmetric(left->right, right->left));
    }

    // 迭代法 (利用2个队列实现)
    bool isSymmetric_I(TreeNode* root){
        if (!root) return true;
        queue<TreeNode*> q1, q2;
        q1.push(root->left); q2.push(root->right);
        while (!q1.empty() && !q2.empty()){
            TreeNode* node1 = q1.front(); q1.pop();
            TreeNode* node2 = q2.front(); q2.pop();
            if (!node1 && !node2) continue;
            if ((node1 && !node2) || (!node1 && node2) || (node1->val != node2->val))
                return false;
            q1.push(node1->left); q2.push(node2->right);
            q1.push(node1->right); q2.push(node2->left);
        }
        return true;
    }
};
