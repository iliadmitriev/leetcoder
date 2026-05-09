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
    void inorder(TreeNode* node, std::function<void(int)> cb) {
        if (!node) {
            return;
        }

        inorder(node->left, cb);
        cb(node->val);
        inorder(node->right, cb);
    }

public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;

        inorder(root, [&res](int val) -> void {
            res.push_back(val);
        });
        return res;
    }
};