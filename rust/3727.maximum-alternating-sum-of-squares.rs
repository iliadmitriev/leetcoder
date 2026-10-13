impl Solution {
    pub fn max_alternating_sum(mut nums: Vec<i32>) -> i64 {
        let h = nums.len() / 2;
        let (less, median, greater) = nums.select_nth_unstable_by_key(h, |v| v.abs());

        let median = (*median as i64) * (*median as i64);
        let left: i64 = less.iter().map(|&v| (v as i64) * (v as i64)).sum();
        let right: i64 = greater.iter().map(|&v| (v as i64) * (v as i64)).sum();

        median + right - left
    }
}