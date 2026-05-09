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
    int averageOfSubtree(TreeNode* root) {
        stack<pair<TreeNode*, bool>> st;
        stack<pair<int, int>> data;

        st.push({root, false});
        int res = 0;

        while (!st.empty()) {
            auto [node, ret] = st.top(); st.pop();

            // if value returned
            if (ret) {
                int total = node->val; int count = 1;
                if (node->left) {
                    total += data.top().first;
                    count += data.top().second;
                    data.pop();
                }
                if (node->right) {
                    total += data.top().first;
                    count += data.top().second;
                    data.pop();
                }
                if (total / count == node->val) {
                    res++;
                }
                data.push({total, count});
                continue;
            }

            // if called
            st.push({node, true});
            if (node->right) {
                st.push({node->right, false});
            }
            if (node->left) {
                st.push({node->left, false});
            }
        }

        return res;
    }
};