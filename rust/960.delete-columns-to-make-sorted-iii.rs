use std::cmp;

impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let rows = strs.len();
        let cols = strs.first().unwrap().len();

        let mut removed = cols - 1; // worst case remove all but one

        let mut dp = vec![1; cols];

        for i in 1..cols {
            for j in 0..i {
                let mut order = true;

                for k in 0..rows {
                    if strs[k].as_bytes()[j] > strs[k].as_bytes()[i] {
                        order = false;
                        break;
                    }
                }

                if order {
                    dp[i] = cmp::max(dp[i], dp[j] + 1);
                }
            }

            removed = cmp::min(removed, cols - dp[i]);
        }

        removed as i32
    }
}