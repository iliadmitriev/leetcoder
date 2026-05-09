impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        let t1: Vec<i32> = s1.bytes().map(|b| b as i32).collect();
        let t2: Vec<i32> = s2.bytes().map(|b| b as i32).collect();

        let m = t1.len();
        let n = t2.len();

        let mut dp = vec![vec![0i32; n + 1]; m + 1];

        // fill with base case
        for i in (0..m).rev() {
            dp[i][n] = dp[i + 1][n] + t1[i];
        }

        for j in (0..n).rev() {
            dp[m][j] = dp[m][j + 1] + t2[j];
        }

        // minimize bottom-up

        for i in (0..m).rev() {
            for j in (0..n).rev() {
                if t1[i] == t2[j] {
                    dp[i][j] = dp[i + 1][j + 1];
                } else {
                    dp[i][j] = std::cmp::min(t1[i] + dp[i + 1][j], t2[j] + dp[i][j + 1]);
                }
            }
        }

        return dp[0][0];
    }
}