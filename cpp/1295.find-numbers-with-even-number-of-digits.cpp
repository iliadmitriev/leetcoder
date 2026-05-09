#include <cmath>
#include <cstdlib>
#include <vector>
using std::vector;

class Solution {
public:
  int findNumbers(vector<int> &nums) {
    int total = 0;

    for (int num : nums) {
      if (int(std::log10(num)) % 2 == 1) {
        total++;
      }
    }

    return total;
  }
};