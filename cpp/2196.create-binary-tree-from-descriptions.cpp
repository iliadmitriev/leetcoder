
#pragma GCC optimize("03")
#pragma GCC target("avx")
#pragma GCC target("-fsplit-loops")

#include <unordered_map>
#include <unordered_set>
#include <vector>

using std::unordered_map;
using std::unordered_set;
using std::vector;

class Solution {
public:
  TreeNode *createBinaryTree(vector<vector<int>> &descriptions) {
    TreeNode *root = NULL;

    if (descriptions.empty()) {
      return root;
    }

    unordered_set<int> hasParent;
    unordered_map<int, TreeNode *> tree;

    for (auto &desc : descriptions) {
      hasParent.insert(desc[1]);

      // if parent node hasn't been created
      if (!tree.count(desc[0])) {
        tree[desc[0]] = new TreeNode(desc[0]);
      }

      // if child node hasn't been created
      if (!tree.count(desc[1])) {
        tree[desc[1]] = new TreeNode(desc[1]);
      }

      if (desc[2]) {
        tree[desc[0]]->left = tree[desc[1]];
      } else {
        tree[desc[0]]->right = tree[desc[1]];
      }
    }

    for (auto &desc : descriptions) {
      if (hasParent.find(desc[0]) == hasParent.end()) {
        root = tree[desc[0]];
      }
    }

    return root;
  }
};