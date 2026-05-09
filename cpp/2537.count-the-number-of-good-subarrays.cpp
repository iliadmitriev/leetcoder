#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
public:
  long long countGood(vector<int> &nums, int k) {
    int n = nums.size();
    long res = 0;
    long pairs = 0;
    unordered_map<int, int> win;

    for (int left = 0, right = 0; right < n; right++) {

      pairs += win[nums[right]];
      win[nums[right]]++;

      while (pairs >= k) {
        win[nums[left]]--;
        pairs -= win[nums[left]];
        left++;
      }

      res += left;
    }

    return res;
  }
};