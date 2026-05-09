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
    int diameterOfBinaryTree(TreeNode* root) {
        int res = 0;

        stack<pair<TreeNode*, bool>> st;
        st.push({root, false});

        unordered_map<TreeNode*, int> ret;
        ret[NULL] = -1;

        while (!st.empty()) {
            auto [node, pr] = st.top(); st.pop();

            if (pr) {
                int left = ret[node->left];
                int right = ret[node->right];
                res = max(res, left + right + 2);
                ret[node] = max(left, right) + 1;

            } else {
                st.push({node, true});

                if (node->right) {
                    st.push({node->right, false});
                }

                if (node->left) {
                    st.push({node->left, false});
                }
            }
        }

        return res;
    }
};