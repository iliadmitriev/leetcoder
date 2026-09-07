impl Solution {
    pub fn distinct_subseq_ii(s: String) -> i32 {
        let MOD = (1_000_000_007) as i64;
        let BASE = b'a';
        let s: Vec<_> = s.bytes().collect();

        let mut dp = 1 as i64;
        let mut last = vec![0i64; 26];
        let mut prev = dp; 

        for (i, &ch) in s.iter().enumerate() {
          prev = dp;
          dp *= 2;

          dp -= last[(ch - BASE) as usize];
          dp += MOD;
          dp %= MOD;

          last[(ch - BASE) as usize] = prev;
        }

        ((dp + MOD - 1) % MOD) as i32
    }
}