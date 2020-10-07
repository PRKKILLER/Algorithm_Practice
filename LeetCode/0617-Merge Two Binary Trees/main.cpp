//
// Created by 薛智钧 on 2020/4/6.
//

struct TreeNode{
    int val;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

/*
 * Given two binary trees and imagine that when you put one of them to cover the other,
 * some nodes of the two trees are overlapped while the others are not.

 You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
 then sum node values up as the new value of the merged node. Otherwise,
 the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
 * */

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (!t1 && !t2) return nullptr;
        else if (t1 && !t2) return t1;
        else if (!t1 && t2) return t2;

        t1->val += t2->val;
        t1->left = mergeTrees(t1->left, t2->left);
        t1->right = mergeTrees(t1->right, t2->right);
        return t1;
    }

    // 建立新节点
    TreeNode* mnergeTrees(TreeNode* t1, TreeNode* t2){
        if (!t1 && !t2) return nullptr;

        auto* node = new TreeNode((t1 ? t1->val : 0) + (t2 ? t2->val : 0));
        node->left = mergeTrees(t1 ? t1->left : nullptr, t2 ? t2->left : nullptr);
        node->right = mergeTrees(t1 ? t1->right : nullptr, t2 ? t2->right : nullptr);
        return node;
    }
};