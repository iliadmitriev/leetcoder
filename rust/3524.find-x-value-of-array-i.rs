impl Solution {
    pub fn result_array(nums: Vec<i32>, k: i32) -> Vec<i64> {
        let k = k as usize;
        if k == 1 {
            let n = nums.len() as i64;
            return vec![n * (n + 1) / 2];
        }

        let mut res = vec![0i64; k];
        // state (switching between previous and current with parity flag index):
        // current i & 1
        // previous i & 1 ^ 1
        let mut dp = vec![vec![0i64; k]; 2];

        for (i, &num) in nums.iter().enumerate() {
            dp[i & 1].fill(0); // reset current state

            let j = num as usize % k;
            dp[i & 1][j] += 1; // count remainder of the current number

            for r in (0..k) {
                // if previous state
                if dp[i & 1 ^ 1][r] > 0 {
                    let j = num as usize * r % k; // remainder of current product (num * r)
                    dp[i & 1][j] += dp[i & 1 ^ 1][r];
                }
            }

            // append current state to result
            for r in (0..k) {
                res[r] += dp[i & 1][r];
            }
        }

        res
    }
}
