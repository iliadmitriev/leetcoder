
#include <deque>
#include <iostream>
#include <vector>

using std::deque, std::vector;

static const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  vector<int> largestValues(TreeNode *root) {
    if (!root) {
      return {};
    }

    vector<int> levelMax;
    deque<TreeNode *> q{root};

    while (!q.empty()) {

      int curMax = q.front()->val;

      for (int sz = q.size(); sz; sz--) {
        TreeNode *node = q.front();
        q.pop_front();

        if (curMax < node->val) {
          curMax = node->val;
        }

        if (node->left) {
          q.push_back(node->left);
        }

        if (node->right) {
          q.push_back(node->right);
        }
      }

      levelMax.push_back(curMax);
    }

    return levelMax;
  }
};