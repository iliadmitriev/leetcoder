#include <vector>

using namespace std;

class Solution {
public:
  int minOperations(vector<int> &nums, int k) {
    int out = 0;
    for (auto num : nums) {
      out ^= num;
    }

    out ^= k;

    int n = 0;
    while (out) {
      out &= out - 1;
      n++;
    }

    return n;
  }
};