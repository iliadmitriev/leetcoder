#include <vector>

using std::vector;

class Solution {
public:
  int minimumOperations(vector<int> &nums) {
    int res = 0;

    for (auto it = nums.begin(); it != nums.end(); it++) {
      if (*it % 3)
        res++;
    }

    return res;
  }
};