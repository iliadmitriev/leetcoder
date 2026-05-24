impl Solution {
    pub fn max_jumps(arr: Vec<i32>, d: i32) -> i32 {
        let n = arr.len();
        let d = d as usize;

        let mut indices: Vec<usize> = (0..n).collect();
        indices.sort_by_key(|&k| arr[k]);

        let mut dp = vec![0; n];

        indices.iter().for_each(|&i| {
            let height = arr[i];

            // scan i-d .. i (reverse order)
            let left_best = (i.saturating_sub(d)..i)
                .rev()
                .take_while(|&j| arr[j] < height)
                .fold((i32::MIN, 0), |(max_val, best), j| {
                    let val = arr[j];
                    if val >= max_val {
                        (val, best.max(dp[j]))
                    } else {
                        (max_val, best)
                    }
                })
                .1;

            // scan i+1 .. i+d
            let right_best = (i + 1..(i + d + 1).min(n))
                .take_while(|&j| arr[j] < height)
                .fold((i32::MIN, 0), |(max_val, best), j| {
                    let val = arr[j];
                    if val >= max_val {
                        (val, best.max(dp[j]))
                    } else {
                        (max_val, best)
                    }
                })
                .1;

            dp[i] = 1 + left_best.max(right_best);
        });

        dp.into_iter().max().unwrap_or_default()
    }
}
