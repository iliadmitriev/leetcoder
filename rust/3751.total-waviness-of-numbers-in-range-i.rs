impl Solution {
    pub fn total_waviness(num1: i32, num2: i32) -> i32 {
      (num1..=num2)
        .map(|mut x| {
          if (x < 101) {
            return 0;
          }

          let mut count = 0;
          let mut r2 = x % 10;
          x /= 10;
          let mut r1 = x % 10;
          x /= 10;
          let mut r;

          while (x > 0) {
            r = x % 10;
            x /= 10;

            if (r2 < r1 && r1 > r) || (r2 > r1 && r1 < r) {
              count += 1;
            }

            (r2, r1) = (r1, r);
          }

          count
        })
        .sum()
    }
}