class Solution {
public:
    int findMin(vector<int>& nums) {
      int lo = 0, hi = nums.size() - 1;
      int mid;

      while (lo < hi) {
        mid = (lo + hi) / 2;

        if (nums[mid] < nums[hi]) {
          hi = mid;
        } else if (nums[mid] > nums[hi]) {
          lo = mid + 1;
        } else {
          hi--;
        }
      }

      return nums[lo];
    }
};