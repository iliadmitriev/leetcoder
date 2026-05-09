
#include <deque>
#include <vector>

using std::deque, std::vector, std::unordered_map;

class Solution {
public:
  int minimumOperations(TreeNode *root) {
    if (!root) {
      return 0;
    }

    deque<TreeNode *> q = {root};
    int swaps = 0;

    while (!q.empty()) {
      int n = q.size();
      vector<int> level;
      level.reserve(n);

      for (; n; n--) {
        TreeNode *node = q.front();
        q.pop_front();

        level.push_back(node->val);

        if (node->left)
          q.push_back(node->left);
        if (node->right)
          q.push_back(node->right);
      }

      swaps += getSwaps(level);
    }

    return swaps;
  }

private:
  int getSwaps(vector<int> &original) {
    int swaps = 0;
    vector<int> sorted(original);
    std::sort(sorted.begin(), sorted.end());
    unordered_map<int, int> pos;

    for (int i = 0; i < original.size(); i++) {
      pos[original[i]] = i;
    }

    for (int i = 0; i < original.size(); i++) {
      if (original[i] == sorted[i]) {
        continue;
      }

      int j = pos[sorted[i]]; // real position of what should be at the
                              // current position
      pos[original[i]] = j;
      pos[original[j]] = i;
      std::swap(original[i], original[j]);

      swaps++;
    }

    return swaps;
  }
};