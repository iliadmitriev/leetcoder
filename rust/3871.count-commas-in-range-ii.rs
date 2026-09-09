impl Solution {
    pub fn count_commas(n: i64) -> i64 {
        let mut exp = 1000 as i64;
        let mut p = 1 as i64;
        let mut nexp = exp * 1000;
        let mut res = 0;

        while (exp <= n) {
          // next exponent is current * 1000 limited by n (+1 inclusive)
          nexp = (exp * 1000).min(n + 1);

          res += (nexp - exp) * p;

          p += 1;
          exp = nexp;
        }

        res
    }
}