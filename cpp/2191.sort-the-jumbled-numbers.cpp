#include <algorithm>
#include <string>
#include <utility>
#include <vector>

using std::sort;
using std::string;
using std::vector;

class Solution {

public:
  vector<int> sortJumbled(vector<int> &mapping, vector<int> &nums) {

    int n = nums.size();
    vector<std::pair<int, int>> tmp;
    tmp.reserve(n);

    for (int i = 0; i < n; ++i) {
      int num = nums[i];

      if (num == 0) {
        tmp.push_back({mapping[num], i});
        continue;
      }

      int mappedNum = 0;
      for (int place = 1; num; place *= 10) {
        mappedNum += mapping[num % 10] * place;
        num /= 10;
      }

      tmp.push_back({mappedNum, i});
    }

    sort(tmp.begin(), tmp.end());
    vector<int> res;
    res.reserve(n);
    for (auto &t : tmp) {
      res.push_back(nums[t.second]);
    }

    return res;
  }
};