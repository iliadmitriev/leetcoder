class Solution {
private:
  bool dfs(ListNode *head, TreeNode *root) {
    if (!head) {
      return true;
    }

    if (!root) {
      return false;
    }

    if (root->val == head->val) {
      return dfs(head->next, root->left) || dfs(head->next, root->right);
    }

    return false;
  }

public:
  bool isSubPath(ListNode *head, TreeNode *root) {
    if (!root) {
      return false;
    }

    return dfs(head, root) || isSubPath(head, root->left) ||
           isSubPath(head, root->right);
  }
};