
class Solution {
public:
  int maxDepth(Node *root) {
    if (!root) {
      return 0;
    }

    int resMax = 0;
    for (auto child : root->children) {
      resMax = max(resMax, maxDepth(child));
    }

    return resMax + 1;
  }
};