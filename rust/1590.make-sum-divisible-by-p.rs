
use std::collections::HashMap;

impl Solution {
    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {
        let sum = nums.iter().map(|x| *x as i64).sum::<i64>();
        let p = p as i64;
        let rem = sum % p;
        let n = nums.len() as i32;

        if rem == 0 {
            return 0;
        }

        if sum < p {
            return -1;
        }

        let mut cache = HashMap::new();
        cache.insert(0, -1);

        let mut sum = 0;
        let mut min_len = n;

        for (i, &num) in nums.iter().enumerate() {
            sum = (sum + num as i64) % p;
            sum = (sum + p) % p; // ensure sum is non-negative

            let prefix = (sum + p - rem) % p;

            if let Some(&j) = cache.get(&prefix) {
                min_len = min_len.min(i as i32 - j);
            }

            cache.insert(sum, i as i32);
        }

        if min_len == n {
            return -1;
        }

        min_len
    }
}