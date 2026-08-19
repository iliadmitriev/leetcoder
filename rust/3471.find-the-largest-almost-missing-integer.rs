use std::collections::HashMap;
use std::cmp;

impl Solution {
    pub fn largest_integer(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();

        if n as i32 == k {
          return nums.iter().max().copied().unwrap_or(-1);
        }

        let mut unique = HashMap::<i32, i32>::new();
        for &x in nums.iter() {
          *unique.entry(x).or_insert(0) += 1;
        }

        if k == 1 {
          let mut mm = -1;
          for &x in nums.iter() {
            if unique.get(&x).copied().unwrap_or(0) == 1 {
              mm = mm.max(x);
            }
          }
          return mm;
        }

        let mut c1 = nums.first().copied().unwrap_or(-1);
        let mut c2 = nums.last().copied().unwrap_or(-1);

        if unique.get(&c1).copied().unwrap_or(0) > 1 {
          c1 = -1;
        }

        if unique.get(&c2).copied().unwrap_or(0) > 1 {
          c2 = -1;
        }

        cmp::max(c1, c2)
    }
}