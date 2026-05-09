class Solution {
private:
  void preorder(TreeNode *node, unordered_map<int, int> &heights,
                int &curMaxHeight, int curHeight, bool leftOrder) {
    if (!node) {
      return;
    }

    heights[node->val] = std::max(heights[node->val], curMaxHeight);
    curMaxHeight = std::max(curMaxHeight, curHeight);

    if (leftOrder) {
      preorder(node->left, heights, curMaxHeight, curHeight + 1, leftOrder);
      preorder(node->right, heights, curMaxHeight, curHeight + 1, leftOrder);
    } else {
      preorder(node->right, heights, curMaxHeight, curHeight + 1, leftOrder);
      preorder(node->left, heights, curMaxHeight, curHeight + 1, leftOrder);
    }
  };

public:
  vector<int> treeQueries(TreeNode *root, vector<int> &queries) {
    int curMaxHeight = 0;
    unordered_map<int, int> heights;

    preorder(root, heights, curMaxHeight, 0, true);
    curMaxHeight = 0;
    preorder(root, heights, curMaxHeight, 0, false);

    vector<int> res(queries.size(), 0);
    for (int i = 0; i < queries.size(); i++) {
      res[i] = heights[queries[i]];
    }

    return res;
  }
};