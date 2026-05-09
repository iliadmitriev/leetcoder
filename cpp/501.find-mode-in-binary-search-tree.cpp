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
    void tree_iter(TreeNode* root, std::function<void(TreeNode*)> fn) {
        if (!root) {
            return;
        }
        std::stack<pair<TreeNode*, bool>> st;
        st.push({root, false});
        while (!st.empty()) {
            auto [node, done] = st.top(); st.pop();

            if (done) {
                fn(node);
            } else {
                if (node->right) {
                    st.push({node->right, false});
                }
                st.push({node, true});
                if (node->left) {
                    st.push({node->left, false});
                }
            }
        }
    }

public:
    vector<int> findMode(TreeNode* root) {
        vector<int> res;
        int count = 0, max_count = 0;
        int prev = numeric_limits<int>::min();

        tree_iter(root, [&](auto node) {
            if (node->val == prev) {
                count++;
            } else {
                count = 1;
            }

            if (count > max_count) {
                res.clear();
                res.push_back(node->val);
                max_count = count;
            } else if (count == max_count) {
                res.push_back(node->val);
            }
            prev = node->val;
        });
        return res;
    }
};