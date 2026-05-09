#include <vector>

using std::vector;

class Solution {
public:
  int minOperations(vector<int> &nums, int k) {

    int counter = 0;
    for (int i = 0; i < nums.size(); ++i) {
      if (nums[i] < k) {
        counter++;
      }
    }

    return counter;
  }
};