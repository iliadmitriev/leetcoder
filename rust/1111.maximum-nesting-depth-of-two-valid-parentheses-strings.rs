impl Solution {
    pub fn max_depth_after_split(seq: String) -> Vec<i32> {
        let n = seq.len();
        let mut res = vec![-1; n];
        let mut depth = 0;

        for (i, ch) in seq.chars().enumerate() {
            match ch {
                '(' => {
                    depth = 1 - depth;
                    res[i] = depth;
                }
                ')' => {
                    res[i] = depth;
                    depth = 1 - depth;
                }
                _ => unreachable!(),
            }
        }

        res
    }
}
