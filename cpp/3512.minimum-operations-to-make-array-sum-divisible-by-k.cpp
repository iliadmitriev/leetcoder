#include <numeric>
#include <vector>
using std::vector;

class Solution {
public:
  int minOperations(vector<int> &nums, int k) {
    if (k == 1) {
      return 0;
    }

    int sum = std::reduce(nums.begin(), nums.end(), 0);
    return (k + sum % k) % k;
  }
};