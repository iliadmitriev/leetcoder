#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;

class Solution {
public:
  int sumOfUnique(vector<int> &nums) {
    unordered_map<int, int> count;
    for (int x : nums) {
      count[x]++;
    }

    int res = 0;
    for (auto [k, v] : count) {
      if (v == 1) {
        res += k;
      }
    }

    return res;
  }
};