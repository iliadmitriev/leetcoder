#include <cmath>
#include <csignal>
#include <numeric>
#include <vector>

using std::vector;

class Solution {
public:
  int minimumSize(vector<int> &nums, int maxOperations) {
    const long total = std::accumulate(nums.begin(), nums.end(), 0L);
    const long count = nums.size();

    if (count + maxOperations >= total) {
      return 1;
    }

    int maxNum = *max_element(nums.begin(), nums.end());

    long lower =
        total / (count + maxOperations) + (total % (count + maxOperations) > 0);

    long upper = total / maxOperations + (total % maxOperations > 0);

    int lo = std::max(1, int(lower) - 1);
    int hi = std::min(int(upper), maxNum) + 1;

    // int lo = 1;
    // int hi = *max_element(nums.begin(), nums.end()) + 1;

    int res = lo;
    long mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (canDivide(nums, mid, maxOperations)) {
        res = mid;
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return res;
  }

private:
  bool canDivide(const vector<int> &nums, int limit, int maxOperations) {
    int ops = 0;

    for (const int num : nums) {
      ops += (num / limit) - (num % limit == 0); // math.ceil(num / limit) - 1

      if (ops > maxOperations) {
        return false;
      }
    }

    return true;
  }
};