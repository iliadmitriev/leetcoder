#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;

class Solution {
public:
  bool checkSubarraySum(vector<int> &nums, int k) {
    int acc = 0;
    unordered_map<int, int> cache{{0, 0}};

    for (int i = 0; i < nums.size(); i++) {
      acc += nums[i];
      acc %= k;

      if (!cache.count(acc)) {
        cache[acc] = i + 1;
      } else if (cache[acc] < i) {
        return true;
      }
    }

    return false;
  }
};