class Solution {
public:
  int firstMissingPositive(vector<int> &nums) {
    int n = nums.size();

    // get rid of negative numbers, set them to 0
    for (int i = 0; i < n; i++) {
      if (nums[i] < 0) {
        nums[i] = 0;
      }
    }

    // if absolute value of a number is in the range of 1 to n inclusive
    // set the number at than index - 1 to negative
    for (int i = 0; i < n; i++) {
      int num = abs(nums[i]);
      if (num >= 1 && num <= n) {
        if (nums[num - 1] > 0) {
          nums[num - 1] = -nums[num - 1];
        } else if (nums[num - 1] == 0) {
          nums[num - 1] = -n - 1;
        }
      }
    }

    // find first missing positive number
    for (int i = 1; i <= n; i++) {
      if (nums[i - 1] >= 0) {
        return i;
      }
    }

    return n + 1;
  }
};