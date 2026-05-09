class Solution {
public:
  TreeNode *bstFromPreorder(vector<int> &preorder) {
    function<TreeNode *(vector<int> &, int, int &)> helper;

    helper = [&helper](vector<int> &preorder, int bound,
                       int &pos) -> TreeNode * {
      if (pos >= preorder.size() || preorder[pos] > bound) {
        return nullptr;
      }

      int val = preorder[pos++];
      TreeNode *root = new TreeNode(val);

      root->left = helper(preorder, root->val, pos);
      root->right = helper(preorder, bound, pos);

      return root;
    };

    int pos = 0;
    return helper(preorder, numeric_limits<int>::max(), pos);
  }
};