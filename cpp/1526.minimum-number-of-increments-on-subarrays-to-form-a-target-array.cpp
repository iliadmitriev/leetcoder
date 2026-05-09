#include <vector>
using std::vector;

class Solution {
public:
  int minNumberOperations(vector<int> &target) {
    int total = 0;
    int prev = 0;

    for (int num : target) {
      if (num > prev) {
        total += num - prev;
      }

      prev = num;
    }

    return total;
  }
};