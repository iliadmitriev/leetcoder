impl Solution {
    pub fn stone_game_viii(mut stones: Vec<i32>) -> i32 {
        let n = stones.len();
        
        for i in (1..n) {
          stones[i] += stones[i - 1];
        }

        let mut dp = vec![0; n];
        dp[n - 1] = stones[n - 1]; // base solution: take all

        for i in (1..n-1).rev() {
          dp[i] = dp[i + 1].max(stones[i] - dp[i + 1]); 
        }

        dp[1]
    }
}