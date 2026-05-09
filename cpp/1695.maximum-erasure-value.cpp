#include <unordered_map>
#include <vector>
using std::vector, std::unordered_map;

class Solution {
public:
  int maximumUniqueSubarray(vector<int> &nums) {
    int maxUnique = 0;

    int cur = 0, left = 0;
    unordered_map<int, int> cnt;

    for (int right = 0; right < nums.size(); right++) {
      cur += nums[right];
      cnt[nums[right]]++;

      while (cnt[nums[right]] > 1) {
        cur -= nums[left];
        cnt[nums[left]]--;
        left++;
      }

      maxUnique = std::max(maxUnique, cur);
    }

    return maxUnique;
  }
};