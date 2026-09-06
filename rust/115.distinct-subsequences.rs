use std::collections::HashSet;

impl Solution {
    pub fn num_distinct(s: String, t: String) -> i32 {
        // rebuild the string s
        // filter unusefull characters
        let tt: HashSet<char> = t.chars().collect();
        let s: Vec<_> = s.chars().filter(|c| tt.contains(c)).collect();
        let t: Vec<_> = t.chars().collect();

        let m = s.len();
        let n = t.len();

        // if there is not enough characters in the source string
        // to build the target
        let diff = (m as i32) - (n as i32);
        if diff < 0 {
            return 0;
        }
        let diff = diff as usize;

        let mut dp = vec![0; n + 1];
        dp[n] = 1; // base case: collectet the target string of size n

        // bottom-up
        for i in (0..m).rev() {
            let start = i.saturating_sub(diff); // clipped to 0 from the bottom
            let end = (i + 1).min(n); // clipped to n from the top

            for j in (start..end) {
                if s[i] == t[j] {
                    dp[j] += dp[j + 1];
                }
            }
        }

        dp[0]
    }
}
