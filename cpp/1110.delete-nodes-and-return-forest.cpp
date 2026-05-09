#include <unordered_set>
#include <vector>

using std::unordered_set;
using std::vector;

class Solution {
private:
  TreeNode *dfsHelper(TreeNode *node, bool isRoot, vector<TreeNode *> &result,
                      const unordered_set<int> &toDel) {
    if (!node) {
      return nullptr;
    }

    if (isRoot && !toDel.count(node->val)) {
      result.push_back(node);
    }

    node->left = dfsHelper(node->left, toDel.count(node->val), result, toDel);
    node->right = dfsHelper(node->right, toDel.count(node->val), result, toDel);

    if (toDel.count(node->val)) {
      delete node;
      return nullptr;
    }

    return node;
  }

public:
  vector<TreeNode *> delNodes(TreeNode *root, vector<int> &to_delete) {
    unordered_set<int> toDel(to_delete.begin(), to_delete.end());
    vector<TreeNode *> result;
    dfsHelper(root, !toDel.count(root->val), result, toDel);
    return result;
  }
};