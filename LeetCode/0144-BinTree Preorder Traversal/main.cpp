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

// Given a binary tree,
// return the preorder traversal of its nodes' values.

class Solution {
public:
    /*递归方法*/
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> preorder; // 先序遍历结果
        trav_recursive(root, preorder);
        return preorder;
    }

    static void trav_recursive(TreeNode* p, vector<int>& v){
        if (!p) return;
        v.push_back(p->val); // 访问当前节点
        trav_recursive(p->left, v); // 不断深入左子树
        trav_recursive(p->right, v); // 不断深入右子树
    }

    /*利用stack先入后出的方法*/
    vector<int> preorderTraversal_1(TreeNode* root){
        stack<TreeNode*> tmp; // 辅助栈
        vector<int> preorder; // 先序遍历结果
        if (root) tmp.push(root); // 根节点入栈
        while (! tmp.empty()){
            root = tmp.top(); tmp.pop(); // 取出栈顶节点
            preorder.push_back(root->val); // 访问栈顶节点
            if(root->right) tmp.push(root->right); // 右孩子先入栈，后出栈
            if(root->left) tmp.push(root->left);// 左孩子后入栈，先出栈
        }
        return preorder;
    }

    /*利用辅助栈，先访问left vine, 再转向右子树*/
    vector<int> preorderTraversal_2(TreeNode* root){
        stack<TreeNode*> tmp; // 辅助栈
        vector<int> preorder; // 先序遍历结果
        while (true){
            while (root){
                preorder.push_back(root->val); // 访问当前节点
                if(root->right) tmp.push(root->right); // 当前节点的右孩子不断入栈
                root = root->left; // 继续向左侧深入
            }
            if (tmp.empty()) break;
            root = tmp.top(); tmp.pop(); // 转向最低节点的右子树
        }
        return preorder;
    }
};