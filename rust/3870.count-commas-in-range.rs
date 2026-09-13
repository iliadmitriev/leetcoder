use std::cmp;

impl Solution {
    pub fn count_commas(n: i32) -> i32 {
       let mut res = 0;
       let mut p = 1; // power
       let mut e = 1000; // exponent

       while (e <= n) {
        let ne = cmp::min(n + 1, e * 1000);

        res += (ne - e) * p;

        e = ne;
        p += 1;
       }

       res
    }
}