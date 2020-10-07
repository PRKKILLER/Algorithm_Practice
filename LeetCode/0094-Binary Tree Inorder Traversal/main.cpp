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

// Given a BinTree, return the inorder traversal of the node value

class Solution {
public:

    // 递归法的中序遍历
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> inorder; // 记录中序遍历结果
        trav_recursive(root, inorder);
        return inorder;
    }

    static void trav_recursive(TreeNode* p, vector<int>& v){
        if (!p) return;
        trav_recursive(p->left, v); // 向左子树深入
        v.push_back(p->val); // 访问当前节点
        trav_recursive(p->right, v); // 转向右子树
    }

    // 先不断深入left vine，再转向右子树
    vector<int> inorderTraversal_1(TreeNode* root){
        vector<int> inorder;
        stack<TreeNode*> tmp;
        while (true){
            goAlongVine(root, tmp);
            if (tmp.empty()) break;
            root = tmp.top(); tmp.pop(); // 当前节点不存在左子树或已经访问过了，因此可以访问
            inorder.push_back(root->val);
            root = root->right; // 转向右子树
        }
        return inorder;
    }

    static void goAlongVine(TreeNode* p, stack<TreeNode*>& v){
        while (p){
            v.push(p);
            p = p->left;
        }
    }

};
