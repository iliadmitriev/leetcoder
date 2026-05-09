
impl Solution {
    pub fn number_of_paths(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let MOD = 1e9 as i32 + 7;
        let m = grid.len();
        let n = grid.first().unwrap().len();

        let mut dp = vec![vec![0; k as usize]; n + 1];
        dp[1][0] = 1;

        for r in 0..m {
            for c in 0..n {
                let mut row = vec![0; k as usize];
                for s in 0..k {
                    let ns = ((s + grid[r][c]) % k) as usize;
                    row[s as usize] = (dp[c][ns] + dp[c + 1][ns]) % MOD;
                }
                dp[c + 1][0..k as usize].clone_from_slice(&row);
            }
        }

        return dp[n][0];
    }
}