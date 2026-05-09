#include <vector>
using std::vector;

class Solution {
public:
  bool kLengthApart(vector<int> &nums, int k) {
    int distance = -1;

    for (int num : nums) {
      if (num == 1) {

        if (distance > 0) {
          return false;
        }
        distance = k;

      } else {
        distance--;
      }
    }

    return true;
  }
};