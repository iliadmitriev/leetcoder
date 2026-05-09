#include <ios>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>
using std::vector, std::unordered_map, std::min, std::accumulate;

const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  int minSubarray(vector<int> &nums, int p) {
    long total = accumulate(nums.begin(), nums.end(), 0L);
    int remain = total % p;

    if (total < p) {
      return -1;
    }

    if (remain == 0) {
      return 0;
    }

    long curSum = 0;
    int prefix = 0;
    int minLen = nums.size();
    unordered_map<int, int> remainMap{{0, -1}};

    for (int i = 0; i < nums.size(); i++) {
      curSum = (curSum + nums[i]) % p;
      prefix = (curSum + p - remain) % p;

      if (remainMap.count(prefix)) {
        minLen = min(minLen, i - remainMap[prefix]);
      }

      remainMap[curSum] = i;
    }

    if (minLen == nums.size()) {
      return -1;
    }

    return minLen;
  }
};