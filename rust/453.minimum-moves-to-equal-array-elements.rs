impl Solution {
    pub fn min_moves(nums: Vec<i32>) -> i32 {
        let size = nums.len() as i32;
        let total: i32 = nums.iter().sum();
        let min = nums.iter().min().unwrap_or(&0);

        total - size * min
    }
}