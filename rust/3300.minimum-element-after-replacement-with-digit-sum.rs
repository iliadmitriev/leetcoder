impl Solution {
    pub fn min_element(nums: Vec<i32>) -> i32 {
        let digit = | x: &i32 | {
          let mut sum = 0;
          let mut x = x.abs();

          while x > 0 {
            sum += x % 10;
            x /= 10;
          }
          
          sum
        };

        nums
          .iter()
          .map(digit)
          .min()
          .unwrap_or_default()
    }
}