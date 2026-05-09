#include <vector>
using std::vector;

class Solution {
public:
  vector<int> numberOfPairs(vector<int> &nums) {
    const int n = 101;

    vector<int> pairs(n, 0);

    for (int num : nums) {
      pairs[num]++;
    }

    vector<int> res = {0, 0};
    for (int pair : pairs) {
      res[0] += pair / 2;
      res[1] += pair % 2;
    }

    return res;
  }
};