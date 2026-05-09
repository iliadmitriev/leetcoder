#include <vector>

using namespace std;

class Solution {
public:
  int findMaxK(vector<int> &nums) {
    int res = -1;
    vector<bool> cache(2000, false);

    for (auto num : nums) {
      if (cache[1000 - num]) {
        if (res < abs(num)) {
          res = abs(num);
        }
      }
      cache[1000 + num] = true;
    }

    return res;
  }
};