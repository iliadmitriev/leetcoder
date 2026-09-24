impl Solution {
    pub fn smallest_index(nums: Vec<i32>) -> i32 {
        let digits = |mut x: i32| {
          let mut y = 0;
          while x > 0 {
            y += x % 10;
            x /= 10;
          }
          y
        };

        for (i, &x) in nums.iter().enumerate() {
          if i as i32 == digits(x) {
            return i as i32
          }
        }

        -1
    }
}