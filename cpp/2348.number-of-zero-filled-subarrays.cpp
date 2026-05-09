#include <vector>
using std::vector;

class Solution {
public:
  long long zeroFilledSubarray(vector<int> &nums) {
    long long total = 0;
    int count = 0;

    for (int num : nums) {
      if (num == 0) {
        count++;
        total += count;
      } else {
        count = 0;
      }
    }

    return total;
  }
};