#include <vector>
using std::vector;

class Solution {
public:
  long long countSubarrays(vector<int> &nums, long long k) {
    long total = 0, cur = 0;

    for (int i = 0, j = 0; i < nums.size(); ++i) {
      cur += nums[i];

      while (j <= i && cur * (i - j + 1) >= k) {
        cur -= nums[j++];
      }

      total += i - j + 1;
    }

    return total;
  }
};