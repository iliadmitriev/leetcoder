
class Solution {
private:
  bool match(TreeNode *root, TreeNode *subRoot) {
    if (!root && !subRoot)
      return true;
    if (!root || !subRoot)
      return false;
    if (root->val != subRoot->val)
      return false;
    return match(root->left, subRoot->left) &&
           match(root->right, subRoot->right);
  }

public:
  bool isSubtree(TreeNode *root, TreeNode *subRoot) {
    if (match(root, subRoot))
      return true;
    if (!root || !subRoot)
      return false;
    return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
  }
};