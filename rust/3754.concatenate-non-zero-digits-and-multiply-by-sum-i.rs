impl Solution {
    pub fn sum_and_multiply(mut n: i32) -> i64 {
        let mut v = Vec::new();

        while n > 0 {
          let d = n % 10;

          if d > 0 {
            v.push(d as i64);
          }

          n /= 10;
        }

        let mut x = 0;
        let mut s = 0;

        while let Some(d) = v.pop() {
          x *= 10;
          x += d;
          s += d;
        }

        x * s
    }
}