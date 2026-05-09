
class Solution {
public:
  long long kthLargestLevelSum(TreeNode *root, int k) {
    if (!root) {
      return 0;
    }

    vector<long long> levels;
    queue<TreeNode *> q{{root}};

    while (q.size()) {
      long long levelSum = 0;
      int levelSize = q.size();

      while (levelSize--) {
        auto node = q.front();
        q.pop();

        levelSum += node->val;

        if (node->left) {
          q.push(node->left);
        }

        if (node->right) {
          q.push(node->right);
        }
      }

      levels.push_back(levelSum);
    }

    sort(levels.begin(), levels.end(), greater<>());

    if (k > levels.size()) {
      return -1;
    }

    return levels[k - 1];
  }
};
