#include <string>
#include <vector>

using std::vector, std::string;

class Solution {
public:
  string triangleType(vector<int> &nums) {
    std::sort(nums.begin(), nums.end());
    if (nums[0] + nums[1] <= nums[2]) {
      return "none";
    }
    if (nums[0] == nums[1] && nums[1] == nums[2]) {
      return "equilateral";
    }
    if (nums[0] == nums[1] || nums[1] == nums[2] || nums[0] == nums[2]) {
      return "isosceles";
    }
    return "scalene";
  }
};