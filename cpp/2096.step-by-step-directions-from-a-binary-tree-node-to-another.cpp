#include <string>

using std::string;

class Solution {
private:
  bool nodePath(TreeNode *root, int value, string &path) {
    if (!root)
      return false;
    if (root->val == value)
      return true;

    path.push_back('L');
    if (nodePath(root->left, value, path))
      return true;
    path.pop_back();

    path.push_back('R');
    if (nodePath(root->right, value, path))
      return true;
    path.pop_back();

    return false;
  }

public:
  string getDirections(TreeNode *root, int startValue, int destValue) {
    string startPath = "", destPath = "";
    nodePath(root, startValue, startPath);
    nodePath(root, destValue, destPath);

    int i = 0;
    while (i < startPath.length() && i < destPath.length() &&
           startPath[i] == destPath[i])
      i++;

    return string(startPath.length() - i, 'U') +
           string(destPath.begin() + i, destPath.end());
  }
};