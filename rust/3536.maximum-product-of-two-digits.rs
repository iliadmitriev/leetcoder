impl Solution {
    pub fn max_product(n: i32) -> i32 {
        let mut n = n;
        let mut d = 0;
        let mut d1 = 0;
        let mut d2 = 0;

        while n > 0 {
            d = n % 10;
            n /= 10;

            if d >= d1 {
              d2 = d1;
              d1 = d;
            } else if d > d2 {
              d2 = d;
            }
        }

        d1 * d2
    }
}