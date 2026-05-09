#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;

class Solution {
public:
  int countKDifference(vector<int> &nums, int k) {
    int count = 0;
    unordered_map<int, int> cache;

    for (int num : nums) {
      count += cache[num - k];
      count += cache[num + k];
      cache[num]++;
    }

    return count;
  }
};