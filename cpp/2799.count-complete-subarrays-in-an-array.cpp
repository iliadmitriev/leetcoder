#include <vector>
using std::vector;

class Solution {
public:
  int countCompleteSubarrays(vector<int> &nums) {
    const int n = nums.size();
    const int size = *max_element(nums.begin(), nums.end()) + 1;
    vector<int> counter(size, 0), win(size, 0);
    int len = 0, total = 0, cur = 0;

    for (int num : nums) {
      counter[num]++;
      if (counter[num] == 1) {
        len++;
      }
    }

    for (int left = 0, right = 0; right < n; right++) {
      win[nums[right]]++;
      if (win[nums[right]] == 1) {
        cur++;
      }

      while (len == cur) {
        win[nums[left]]--;
        if (win[nums[left]] == 0) {
          cur--;
        }
        left++;
      }

      total += left;
    }

    return total;
  }
};