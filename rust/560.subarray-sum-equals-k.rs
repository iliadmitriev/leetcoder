
use std::collections::HashMap;

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut cur = 0;
        let mut total = 0;
        let mut cache: HashMap<i32, i32> = HashMap::new();
        cache.insert(0, 1);

        for num in nums {
            cur += num;

            total += *cache.entry(cur - k).or_default();
            *cache.entry(cur).or_default() += 1;
        }

        return total;
    }
}