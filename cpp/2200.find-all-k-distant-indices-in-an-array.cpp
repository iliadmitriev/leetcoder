#include <vector>
using std::vector;

class Solution {
public:
  vector<int> findKDistantIndices(vector<int> &nums, int key, int k) {
    vector<int> indices, res;
    int prev = 0;
    const int n = nums.size();

    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == key) {
        indices.push_back(i);
      }
    }

    for (int idx : indices) {
      int left = std::max(prev, idx - k);
      int right = std::min(n, idx + k + 1);

      for (int i = left; i < right; i++) {
        res.push_back(i);
      }

      prev = right;
    }

    return res;
  }
};