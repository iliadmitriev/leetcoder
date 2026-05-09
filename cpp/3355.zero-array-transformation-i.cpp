#include <vector>
using std::vector;

class Solution {
public:
  bool isZeroArray(vector<int> &nums, vector<vector<int>> &queries) {
    const int n = nums.size();
    vector<int> prefix(n + 1, 0);

    for (const auto &q : queries) {
      prefix[q[0]]++;
      prefix[q[1] + 1]--;
    }

    int cur = 0;
    for (int i = 0; i < n; i++) {
      cur += prefix[i];
      if (cur < nums[i])
        return false;
    }

    return true;
  }
};