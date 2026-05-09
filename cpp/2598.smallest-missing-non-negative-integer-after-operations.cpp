#include <vector>
using std::vector;

class Solution {
public:
  int findSmallestInteger(vector<int> &nums, int value) {
    if (value == 1) {
      return nums.size();
    }

    vector<int> freq(value, 0);
    for (int num : nums) {
      num %= value;
      if (num < 0) {
        num += value;
      }

      freq[num]++;
    }

    int minVal = freq.front(), minIdx = 0;
    for (int i = 1; i < value; i++) {
      if (freq[i] < minVal) {
        minVal = freq[i];
        minIdx = i;
      }
    }

    return value * minVal + minIdx;
  }
};