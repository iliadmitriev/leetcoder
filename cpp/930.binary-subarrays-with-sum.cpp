class Solution {
public:
  int numSubarraysWithSum(vector<int> &nums, int goal) {
    int i = 0, j = 0, n = nums.size(), res = 0, count = 0;

    for (; j < n; ++j) {
      if (nums[j] == 1) {
        goal--;
        count = 0;
      }

      while (goal == 0 && i <= j) {
        goal += nums[i];
        i++;
        count++;
        if (i > j - goal + 1) {
          break;
        }
      }

      while (goal < 0) {
        goal += nums[i];
        i++;
      }

      res += count;
    }

    return res;
  }
};