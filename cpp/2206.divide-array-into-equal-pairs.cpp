#include <vector>
using std::vector;

class Solution {
public:
  bool divideArray(vector<int> &nums) {
    vector<int> cnt(501, 0);
    for (auto &num : nums) {
      cnt[num]++;
    }
    for (auto &c : cnt) {
      if (c % 2 != 0) {
        return false;
      }
    }
    return true;
  }
};