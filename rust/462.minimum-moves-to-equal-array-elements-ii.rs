impl Solution {
    pub fn min_moves2(mut nums: Vec<i32>) -> i32 {
        let mid_ix = nums.len() / 2;

        let (_, &mut mid, _) = nums.select_nth_unstable(mid_ix);

        nums.iter().fold(0, |acc, &v| acc + (mid - v).abs())
    }
}