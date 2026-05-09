#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
  int minSwaps(vector<int> &nums) {

    int n = nums.size(), countOnes = std::count(nums.begin(), nums.end(), 1);

    int ones = 0, l = 0, res = n - countOnes;
    for (int r = 0; r < n * 2; r++) {

      ones += nums[r % n] == 1;
      if (r - l + 1 > countOnes) {
        ones -= nums[l % n] == 1;
        l++;
      }

      if (r - l + 1 == countOnes) {
        res = std::min(res, countOnes - ones);
      }
    }

    return res;
  }
};