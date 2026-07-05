impl Solution {
    pub fn paths_with_max_score(board: Vec<String>) -> Vec<i32> {
        let n = board.len();
        let board: Vec<Vec<u8>> = board.iter().map(|s| s.bytes().collect()).collect();
        const MOD: i32 = 1_000_000_007;

        // dp[i][j] = (max_score, count)
        let mut dp = vec![vec![(i32::MIN, 0i32); n]; n];
        dp[n - 1][n - 1] = (0, 1);

        for i in (0..n).rev() {
            for j in (0..n).rev() {
                if board[i][j] == b'X' || (i == n - 1 && j == n - 1) {
                    continue;
                }

                let mut best = i32::MIN;
                let mut ways = 0i32;

                for &(di, dj) in &[(1, 0), (0, 1), (1, 1)] {
                    let pi = i + di;
                    let pj = j + dj;
                    if pi < n && pj < n && dp[pi][pj].0 != i32::MIN {
                        let (score, count) = dp[pi][pj];
                        if score > best {
                            best = score;
                            ways = count;
                        } else if score == best {
                            ways = (ways + count) % MOD;
                        }
                    }
                }

                if best != i32::MIN {
                    let val = if board[i][j] >= b'1' && board[i][j] <= b'9' {
                        (board[i][j] - b'0') as i32
                    } else {
                        0
                    };
                    dp[i][j] = (best + val, ways);
                }
            }
        }

        if dp[0][0].0 == i32::MIN {
            vec![0, 0]
        } else {
            vec![dp[0][0].0, dp[0][0].1]
        }
    }
}
