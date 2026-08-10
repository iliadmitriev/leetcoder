impl Solution {
    pub fn winner_square_game(n: i32) -> bool {
        let n = n as usize;
        let s = n.isqrt();
        let mut dp = vec![false; n + 1];

        for i in (0..n) {
            if dp[i] {
                continue;
            }

            for k in (1..=s) {
                if i + k * k <= n {
                    dp[i + k * k] = true;
                } else {
                    break;
                }
            }

        }

        dp[n]
    }
}