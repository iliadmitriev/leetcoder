impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut lo: usize = 0;
        let mut hi: usize = nums.len().checked_sub(1).unwrap_or_default();
        let mut mid: usize;

        while (lo <= hi) {
            mid = (lo + hi) / 2;

            if nums[mid] == target {
                return mid as i32;
            }

            // right is continuous; left if broken
            if nums[lo] > nums[mid] {
                // test target is in the right
                if nums[mid] < target && target <= nums[hi] {
                    lo = mid + 1; // get rid of the left
                // otherwise
                } else {
                    hi = mid - 1; // get rid of the right
                }
                // left is continuous; right is broken
            } else {
                // test target is in the left
                if nums[lo] <= target && target < nums[mid] {
                    hi = mid - 1; // get rid of the right
                // otherwise
                } else {
                    lo = mid + 1; // get rid of the left
                }
            }
        }

        -1
    }
}
