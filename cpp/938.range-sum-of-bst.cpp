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
    int rangeSumBST(TreeNode* root, int low, int high) {
        if (root == NULL) {
            return 0;
        }

        int res = 0;
        stack<TreeNode*> st({root});
        TreeNode* node;
        
        while (!st.empty()) {
            node = st.top(); st.pop();

            if (low <= node->val && node->val <= high) {
                res += node->val;
            }

            if (node->right != NULL && node->val <= high) {
                st.push(node->right);
            }

            if (node->left != NULL && low <= node->val) {
                st.push(node->left);
            }
        }

        return res;
    }
};