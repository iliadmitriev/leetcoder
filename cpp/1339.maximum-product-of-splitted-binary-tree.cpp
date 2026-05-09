
const static int MOD = int(1e9) + 7;

class Solution {
public:
  int maxProduct(TreeNode *root) {
    vector<long> sums;
    getNodeSums(root, sums);

    long total = sums.back();
    long maxProd = 0;

    for (long sum : sums) {
      maxProd = std::max(maxProd, sum * (total - sum));
    }

    return maxProd % MOD;
  }

private:
  long getNodeSums(TreeNode *node, vector<long> &sums) {
    if (!node) {
      return 0;
    }

    long res = node->val + getNodeSums(node->left, sums) +
               getNodeSums(node->right, sums);

    sums.push_back(res % MOD);

    return res;
  }
};