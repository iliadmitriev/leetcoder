#include <map>
#include <vector>

using std::map;
using std::max;
using std::vector;

class Solution {
public:
  int longestSubarray(vector<int> &nums, int limit) {
    int logest = 0;
    map<int, int> window;

    for (int r = 0, l = 0; r < nums.size(); r++) {
      window[nums[r]]++;

      while (window.rbegin()->first - window.begin()->first > limit) {
        window[nums[l]]--;
        if (window[nums[l]] == 0) {
          window.erase(nums[l]);
        }
        l++;
      }

      logest = max(logest, r - l + 1);
    }

    return logest;
  }
};
