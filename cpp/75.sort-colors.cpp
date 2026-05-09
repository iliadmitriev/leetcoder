#include <vector>
using std::vector;

class Solution {
public:
  void sortColors(vector<int> &nums) {
    vector<int> cnt(3, 0);
    for (int num : nums) {
      cnt[num]++;
    }
    int i = 0;
    for (int j = 0; j < 3; j++) {
      while (cnt[j]--) {
        nums[i++] = j;
      }
    }
  }
};