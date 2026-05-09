#include <vector>
using std::vector;

class Solution {
public:
  vector<int> resultsArray(vector<int> &nums, int k) {
    if (k == 1) {
      return nums;
    }

    int counter = 1;
    int n = nums.size();
    vector<int> res;

    for (int i = 1; i < n; i++) {
      if (nums[i - 1] + 1 == nums[i]) {
        counter++;
      }

      if (i >= k) {
        if (nums[i - k] + 1 == nums[i - k + 1]) {
          counter--;
        }
      }

      if (i + 1 >= k) {
        if (counter == k) {
          res.push_back(nums[i]);
        } else {
          res.push_back(-1);
        }
      }
    }

    return res;
  }
};