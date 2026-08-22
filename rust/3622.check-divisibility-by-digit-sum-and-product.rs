use std::iter::successors;

impl Solution {
    pub fn check_divisibility(n: i32) -> bool {
        let (sum, prod) = successors(Some(n), |&x| if x > 0 { Some(x / 10) } else { None })
            .take_while(|&x| x > 0)
            .map(|x| x % 10)
            .fold((0, 1), |(s, p), d| (s + d, p * d));

        n % (sum + prod) == 0
    }
}
