use std::cmp;

impl Solution {
    pub fn minimum_deletions(nums: Vec<i32>) -> i32 {
        let mut m = nums[0];
        let mut M = nums[0];
        let mut mi = 0;
        let mut Mi = 0;

        for (i, &x) in nums.iter().enumerate() {
            if x < m {
                m = x;
                mi = i;
            } else if x > M {
                M = x;
                Mi = i;
            }
        }

        let n = nums.len() as i32;
        let l = cmp::min(mi, Mi) as i32;
        let r = cmp::max(mi, Mi) as i32;

        cmp::min(
            l + 1 + n - r, /* |===>l+1  n-r<====| */
            cmp::min(
                r + 1, /* |===>l+1===r+1>    | */
                n - l, /* |   <l+1===r+1<====| */
            ),
        )
    }
}
