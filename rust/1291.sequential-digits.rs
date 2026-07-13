use std::collections::VecDeque;

impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let mut q = VecDeque::from_iter(1..10);
        let mut res = Vec::new();

        while let Some(x) = q.pop_front() {
          if low <= x && x <= high {
            res.push(x);
          }

          let d = x % 10 + 1;
          let y = x * 10 + d;

          if d < 10 && y <= high {
            q.push_back(y);
          }
        }

        res
    }
}