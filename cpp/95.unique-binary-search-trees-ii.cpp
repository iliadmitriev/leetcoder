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
    TreeNode* clone_with_offset(TreeNode* root, int offset) {
        if (root == NULL || !offset)
            return root;

        TreeNode* res = new TreeNode();
        // tuple( node, parent, position)
        // position: 0 - left, 1 - right
        std::queue<std::tuple<TreeNode*, TreeNode*, int>>que;
        que.push(std::tuple<TreeNode*, TreeNode*, int>(root, res, 0));

        while (!que.empty()) {
            const auto [node, parent, pos] = que.front(); que.pop();
            
            TreeNode* new_node = new TreeNode(node->val + offset);
            if (parent != NULL)
                pos ? parent->right = new_node : parent->left = new_node;

            if (node->right != NULL)
                que.push(std::tuple<TreeNode*, TreeNode*, int>{node->right, new_node, 1});
            if (node->left != NULL)
                que.push(std::tuple<TreeNode*, TreeNode*, int>{node->left, new_node, 0});
        }

        return res->left;
        
    }

    // TreeNode* clone(TreeNode* node, int offset) {
    //     if (node == nullptr) return nullptr;
    //     TreeNode* new_node = new TreeNode(node->val + offset);
    //     new_node->left = clone(node->left, offset);
    //     new_node->right = clone(node->right, offset);
    //     return new_node;
    // }

public:
    vector<TreeNode*> generateTrees(int n) {
        if (n <= 0)
            return vector<TreeNode*>();


        vector<vector<TreeNode*>> dp(n + 1);
        dp[0].push_back(nullptr);

        for (int nodes = 1; nodes <= n; nodes++)
            for (int root = 1; root <= nodes; root++)
                for (TreeNode* left : dp[root - 1])
                    for (TreeNode* right : dp[nodes - root]) {
                        TreeNode* current = new TreeNode(root);
                        current->left = left;
                        current->right = clone_with_offset(right, root);
                        dp[nodes].push_back(current);
                    }

        return dp[n];
    }
};