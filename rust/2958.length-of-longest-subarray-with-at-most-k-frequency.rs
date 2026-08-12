use std::collections::HashMap;

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();

        if (k as usize >= n) {
            return n as i32;
        }

        let mut j = 0 as usize;
        let mut i = 0 as usize;
        let mut cnt = HashMap::<i32, i32>::new();
        let mut longest = 0 as usize;

        for i in (0..n) {
            *cnt.entry(nums[i]).or_insert(0) += 1;
            
            while *cnt.get(&nums[i]).unwrap() > k {
                *cnt.get_mut(&nums[j]).unwrap() -= 1;
                j += 1;
            }

            longest = longest.max(i - j + 1);
        }
        longest as i32
    }
}