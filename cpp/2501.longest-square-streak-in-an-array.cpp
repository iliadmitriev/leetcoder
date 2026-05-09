#include <unordered_set>
#include <vector>

using std::vector, std::unordered_set;

class Solution {
public:
  int longestSquareStreak(vector<int> &nums) {
    unordered_set<int> cache(nums.begin(), nums.end());
    unordered_set<int> seen;
    const int limit = int(1e5);

    int longest = 0;

    for (int num : nums) {
      if (seen.count(num)) {
        continue;
      }

      seen.insert(num);
      long cur = num;
      int curLen = 1;

      while (cur * cur <= limit && cache.count(cur * cur)) {
        curLen++;
        cur *= cur;
      }

      if (curLen > longest) {
        longest = curLen;
      }
    }

    if (longest < 2) {
      return -1;
    }

    return longest;
  }
};