/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    int dfs(TreeNode* node, int cache) {
        if (!node) {
            return 0;
        }

        cache ^= (1 << node->val);

        int res = 0;
        if (!node->left && !node->right) {
            if ((cache == 0) || ((cache & (cache - 1)) == 0)) {
                res += 1;
            }
        }

        res += dfs(node->left, cache);
        res += dfs(node->right, cache);

        cache ^= (1 << node->val);

        return res;
    }

public:
    int pseudoPalindromicPaths (TreeNode* root) {
        return dfs(root, 0);
    }
};