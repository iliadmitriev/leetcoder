#include <vector>

using std::vector;

class Solution {
public:
  vector<int> resultArray(vector<int> &nums) {
    vector<int> arr1 = {nums[0]}, arr2 = {nums[1]};
    arr1.reserve(nums.size());

    for (int j = 2; j < nums.size(); j++) {
      if (arr1.back() > arr2.back()) {
        arr1.push_back(nums[j]);
      } else {
        arr2.push_back(nums[j]);
      }
    }

    arr1.insert(arr1.end(), arr2.begin(), arr2.end());

    return arr1;
  }
};