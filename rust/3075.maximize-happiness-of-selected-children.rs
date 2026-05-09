
use std::cmp;

impl Solution {
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, k: i32) -> i64 {
        happiness.sort_unstable_by(|a, b| b.cmp(a)); // sort in descending order

        happiness
            .into_iter()
            .take(k as usize)
            .enumerate()
            .map(|(j, value)| ((value - j as i32) as i64).max(0))
            .take_while(|&value| value > 0)
            .sum()
    }
}