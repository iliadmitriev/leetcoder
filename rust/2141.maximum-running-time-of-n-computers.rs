
use std::cmp::min;

impl Solution {
    fn check(t: i64, n: i64, batteries: &Vec<i32>) -> bool {
        let mut sum = 0;
        let taget = t * n;

        for &n in batteries {
            sum += std::cmp::min(t, n as i64);

            if sum >= taget {
                return true;
            }
        }
        false
    }

    pub fn max_run_time(n: i32, mut batteries: Vec<i32>) -> i64 {
        let n = n as i64;
        let total = batteries.iter().map(|i| *i as i64).sum::<i64>();

        let mut lo = 0;
        let mut hi = total / n + 1;
        let mut res = 0;

        while lo < hi {
            let mid = (hi + lo) / 2;

            if Self::check(mid, n, &batteries) {
                res = mid;
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        res
    }
}