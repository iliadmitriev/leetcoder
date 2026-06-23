const MOD: i32 = 1_000_000_007;

impl Solution {
    pub fn zig_zag_arrays(n: i32, l: i32, r: i32) -> i32 {
        let m = (r - l + 1) as usize;

        // dp0 and dp1 represent the number of zigzag arrays ending with a smaller/larger element
        let mut dp0 = vec![1i32; m];
        let mut dp1 = vec![1i32; m];

        // prefix sums for dp0 and dp1 (length m+1, sum[0] = 0)
        let mut sum0 = vec![0i32; m + 1];
        let mut sum1 = vec![0i32; m + 1];

        // iterate over positions 1..n-1 (since we already have initial arrays for length 1)
        for _ in 1..n {
            // compute prefix sums modulo MOD
            for j in 0..m {
                sum0[j + 1] = (sum0[j] + dp0[j]) % MOD;
                sum1[j + 1] = (sum1[j] + dp1[j]) % MOD;
            }

            // update dp arrays using the prefix sums
            for j in 0..m {
                // dp0[j] = (total sum of dp1 - sum of dp1 up to j) % MOD
                // ensure non-negative remainder
                dp0[j] = (sum1[m] + MOD - sum1[j + 1]) % MOD;
                // dp1[j] = prefix sum of dp0 up to j-1 (i.e., sum0[j])
                dp1[j] = sum0[j];
            }
        }

        // sum both arrays and combine
        let ans0 = dp0.iter().fold(0, |acc, &x| (acc + x) % MOD);
        let ans1 = dp1.iter().fold(0, |acc, &x| (acc + x) % MOD);

        (ans0 + ans1) % MOD   
    }
}