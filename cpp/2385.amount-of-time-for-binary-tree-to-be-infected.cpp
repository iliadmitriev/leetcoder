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
    int bfs(unordered_map<int, vector<int>>& gr, int n, int start) {
        unordered_map<int, bool> vis;
        vis[start] = true;

        queue<int> q;
        q.push(start);

        int level = -1;
        int node, k;

        while (!q.empty()) {
            k = q.size();
            for (int i = 0; i < k; i++) {
                node = q.front(); q.pop();

                for (auto child: gr[node]) {
                    if (vis[child]) {
                        continue;
                    }
                    vis[child] = true;
                    q.push(child);
                }
            }
            level++;
        }

        return level;
    }

    int buildGr(unordered_map<int, vector<int>>& gr, TreeNode* root) {
        if (root == NULL) {
            return 0;
        }

        int count = 0;
        stack<pair<TreeNode*, TreeNode*>> q;
        q.push({NULL, root});

        while (!q.empty()) {
            auto [parent, node] = q.top(); q.pop();

            count++;
            if (parent != NULL) {
                gr[node->val].push_back(parent->val);
                gr[parent->val].push_back(node->val);
            }

            if (node->right != NULL) {
                q.push({node, node->right});
            }

            if (node->left != NULL) {
                q.push({node, node->left});
            }
        }

        return count;
    }

public:
    int amountOfTime(TreeNode* root, int start) {
        unordered_map<int, vector<int>> gr;
        int n = buildGr(gr, root);

        return bfs(gr, n, start);
    }
};