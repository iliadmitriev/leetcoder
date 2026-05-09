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
class TreePreorderLeaves {
private:
    stack<TreeNode*> st;

public:
    TreePreorderLeaves(TreeNode* root) {
        if (root != NULL) {
            st.push(root);
        }
    }

    TreeNode* next() {
        TreeNode* node;

        while (!st.empty()) {
            node = st.top(); st.pop();
            
            if (node->right) {
                st.push(node->right);
            }

            if (node->left) {
                st.push(node->left);
            }

            if (!node->left && !node->right) {
                return node;
            }
        }

        return NULL;
    }
};

class Solution {


public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        TreePreorderLeaves it1(root1);
        TreePreorderLeaves it2(root2);

        while (true) {
            TreeNode* node1 = it1.next();
            TreeNode* node2 = it2.next();

            if (node1 == NULL && node2 == NULL) {
                return true;
            }

            if (node1 == NULL || node2 == NULL || node1->val != node2->val) {
                return false;
            }

        }

        return false;
    }
};