#include <numeric>
#include <vector>
using std::vector;

class Solution {
public:
  vector<int> getMaximumXor(vector<int> &nums, int maximumBit) {
    int n = nums.size();
    int mask = (1 << maximumBit) - 1;
    int allXor = 0;
    vector<int> res(n);

    for (int i = 0; i < n; i++) {
      allXor ^= nums[i];
      res[n - i - 1] = allXor ^ mask;
    }

    return res;
  }
};