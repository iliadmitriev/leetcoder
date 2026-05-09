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
public:
    bool isEvenOddTree(TreeNode* root) {
        queue<TreeNode*> que({root});
        bool even = false;

        while (!que.empty()) {

            int n = que.size();
            int pre = even ? numeric_limits<int>::max() : numeric_limits<int>::min();

            for (int i = 0; i < n; i++) {
                auto node = que.front(); que.pop();

                if (even) {
                    if (node->val % 2 == 1 || pre <= node->val) {
                        return false;
                    }
                } else {
                    if (node->val % 2 == 0 || pre >= node->val) {
                        return false;
                    }
                }

                if (node->left) {
                    que.push(node->left);
                }

                if (node->right) {
                    que.push(node->right);
                }

                pre = node->val;
            }

            even = !even;
        }

        return true;
    }
};