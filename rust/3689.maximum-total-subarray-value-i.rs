impl Solution {
    pub fn max_total_value(nums: Vec<i32>, k: i32) -> i64 {
      if let (Some(&min), Some(&max)) = (nums.iter().min(), nums.iter().max()) {
        let max = max as i64;
        let min = min as i64;
        let k = k as i64;

        k * (max - min)
      } else {
        0
      }
    }
}