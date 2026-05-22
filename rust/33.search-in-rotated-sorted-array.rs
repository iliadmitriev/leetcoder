impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut lo = 0;
        let mut hi = if nums.is_empty() { return -1; } else { nums.len() - 1 };

        while (lo <= hi) {
            let mid = lo + (hi - lo) / 2;

            if nums[mid] == target {
                return mid as i32;
            }

            // right half is sorted (no rotation brakes)
            if nums[lo] > nums[mid] {
                // test target is in the right
                if nums[mid] < target && target <= nums[hi] {
                    lo = mid + 1; // get rid of the left
                // otherwise
                } else {
                    hi = mid - 1; // get rid of the right
                }
                // left half is sorted (no rotation brakes)
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
