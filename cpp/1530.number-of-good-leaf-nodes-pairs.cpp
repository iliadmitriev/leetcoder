#include <vector>

using std::pair;
using std::vector;

class Solution {
private:
  pair<int, vector<int>> dfs(TreeNode *node, int depth, int distance) {
    if (!node) {
      return {0, {}};
    }

    if (!node->left && !node->right) {
      return {0, {depth}};
    }

    const auto &[leftCount, leftDepths] = dfs(node->left, depth + 1, distance);
    const auto &[rightCount, rightDepths] =
        dfs(node->right, depth + 1, distance);

    int count = 0;
    for (auto left : leftDepths) {
      for (auto right : rightDepths) {
        if (left + right - 2 * depth <= distance) {
          count++;
        }
      }
    }

    vector<int> depths;
    for (auto left : leftDepths) {
      if (left - depth <= distance) {
        depths.push_back(left);
      }
    }
    for (auto right : rightDepths) {
      if (right - depth <= distance) {
        depths.push_back(right);
      }
    }

    return {count + leftCount + rightCount, depths};
  }

public:
  int countPairs(TreeNode *root, int distance) {
    const auto &[res, _] = dfs(root, 0, distance);
    return res;
  }
};