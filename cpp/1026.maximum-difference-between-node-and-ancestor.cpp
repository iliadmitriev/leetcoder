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
    int maxAncestorDiff(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }

        stack<tuple<TreeNode*, int, int>> st;
        st.push({ root, root->val, root->val });
        int res = 0;

        while (!st.empty()) {
            auto [node, lo, hi] = st.top(); st.pop();

            if (node == NULL) {
                res = max(res, hi - lo);
                continue;
            }

            lo = min(lo, node->val);
            hi = max(hi, node->val);

            st.push({node->right, lo, hi});
            st.push({node->left, lo, hi});
        }

        return res;
    }
};