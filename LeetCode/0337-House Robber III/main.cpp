//
// Created by 薛智钧 on 2020/6/1.
//
#include <iostream>
#include <unordered_map>

using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/*
 *  The thief has found himself a new place for his thievery again.
 *  There is only one entrance to this area, called the "root." Besides the root,
 *  each house has one and only one parent house. After a tour,
 *  the smart thief realized that "all houses in this place forms a binary tree".
 *  It will automatically contact the police if two directly-linked houses
 *  were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
 * */

class Solution {
public:
    // 思路1： trivial solution
    /*
     * 该问题表现了最优子结构的特征：如果我们想从当前的binary tree抢到最多的钱，我们一定也想在当前binary tree的
     * 左子树和右子树得到相同的结果。
     * 解题的关键：如何从rob(root->left)和rob(root->right)得到rob(root)，这样很容易想到，该问题解题需要使用递归
     * 而对于任何一个root节点，只存在两种情况：抢root和不抢root。
     * 如果抢了root，due to the constraint that "we cannot rob any two directly-linked houses",
     * the next level of subtrees that are available would be the four "grandchild-subtrees"
     * (root.left.left, root.left.right, root.right.left, root.right.right).
     * */
    static int rob_1(TreeNode* root) {
        if (!root) return 0;
        int val = 0;
        if (root->left) {
            val += rob_1(root->left->left) + rob_1(root->left->right); // grandchild of root
        }
        if (root->right) {
            val += rob_1(root->right->left) + rob_1(root->right->left);
        }
        return max(root->val + val, rob_1(root->left) + rob_1(root->right));
    }

//  思路2：dp + memo
//  观察可知，在计算最优子结构的时候，我们的计算存在overlapping。
//  即：当计算rob(root->left)的时候，我们也用到了rob(boot->left->left)和rob(root->left->right)
// 因此存在了重复计算，因此可以采用hashmap作为memo保存已经计算过的suboptimal structure

    int rob_2(TreeNode* root) {
        unordered_map<TreeNode*, int> memo;
        return rob_helper(root, memo);
    }

    int rob_helper(TreeNode* root, unordered_map<TreeNode*, int>& memo) {
        if (!root) return 0;
        if (memo.count(root)) return memo[root];

        int val = 0;
        // 计算当前root的grandchild子树的最大值
        if (root->left)
            val += rob_helper(root->left->left, memo) + rob_helper(root->left->right, memo);
        if (root->right)
            val += rob_helper(root->right->left, memo) + rob_helper(root->right->right, memo);
        // 计算当前根节点的最大值
        memo[root] = max(root->val + val, rob_helper(root->left, memo) + rob_helper(root->right, memo));
        return memo[root];
    }

    // 思路3：反思之前的设计
    /*
     * Now let's take one step back and ask why we have overlapping subproblems.
     * If you trace all the way back to the beginning, you'll find the answer lies in the way
     * how we have defined rob(root). As I mentioned, for each tree root,
     * there are two scenarios: it is robbed or is not. rob(root) does not distinguish between
     * these two cases, so "information is lost as the recursion goes deeper and deeper",
     * which results in repeated subproblems.

    If we were able to maintain the information about the two scenarios
     for each tree root, let's see how it plays out.
     Redefine rob(root) as a new function which will return an array of two elements,
     num[0] is the max value while rob this node,
     num[1] is max value while not rob this value.

    Let's relate rob(root) to rob(root.left) and rob(root.right)..., etc.
     For the 1st element of rob(root), we only need to sum up
     the larger elements of rob(root.left) and rob(root.right), respectively,
     since root is not robbed and we are free to rob its left and right subtrees.
     For the 2nd element of rob(root), however, we only need to add up the
     1st elements of rob(root.left) and rob(root.right), respectively,
     plus the value robbed from root itself,
     since in this case it's guaranteed that we cannot rob the nodes of root.left and root.right.
     * */
};

