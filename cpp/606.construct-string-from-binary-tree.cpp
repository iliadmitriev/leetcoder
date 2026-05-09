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
    string tree2str(TreeNode* root) {
        if (root == NULL) {
            return "";
        }

        stringstream res;
        stack<pair<TreeNode*, bool>> st;
        st.push({root, false});

        while (!st.empty()) {

            auto [node, seen] = st.top(); st.pop();

            if (seen) {
                res << ")";
            } else {
                st.push({node, true});

                res << "(" << node->val;

                if (node->left == NULL && node->right != NULL) {
                    res << "()";
                }

                if (node->right) {
                    st.push({node->right, false});
                }

                if (node->left) {
                    st.push({node->left, false});
                }
            }
        }

        string res_str = res.str();
        return res_str.substr(1, res_str.size() - 2);
    }
};