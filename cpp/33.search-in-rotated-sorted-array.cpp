class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lo = 0, hi = nums.size() - 1, mid;

        while (lo <= hi) {
            mid = (lo + hi) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[lo] > nums[mid]) { // right is whole and left is broken
                if (nums[mid] < target &&
                    target <= nums[hi]) { // target is in the right
                    lo = mid + 1;         // get rid of the left part
                } else {                  // otherwise
                    hi = mid - 1;         // get rid of the right part
                }
            } else { // left if whole and right is broken
                if (nums[lo] <= target &&
                    target < nums[mid]) { // target is in the left
                    hi = mid - 1;         // get rid of the right part
                } else {                  // otherwise
                    lo = mid + 1;         // get rid of the left part
                }
            }
        }

        return -1;
    }
};