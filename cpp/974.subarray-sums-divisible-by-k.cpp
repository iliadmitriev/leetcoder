#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;

class Solution {
public:
  int subarraysDivByK(vector<int> &nums, int k) {
    int res = 0, acc = 0;
    unordered_map<int, int> cache = {{0, 1}};

    for (int num : nums) {
      acc = (acc + num) % k;
      acc = (acc + k) % k;
      res += cache[acc];
      ++cache[acc];
    }

    return res;
  }
};