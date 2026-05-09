
impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let rows = strs.len();
        let cols = strs.first().unwrap().len();

        // let strs: Vec<Vec<char>> = strs.into_iter().map(|s| s.chars().collect()).collect();

        (0..cols)
            .filter(|&c| {
                for r in 1..rows {
                    if strs[r - 1].as_bytes()[c] > strs[r].as_bytes()[c] {
                        return true;
                    }
                }

                false
            })
            .count() as i32
    }
}