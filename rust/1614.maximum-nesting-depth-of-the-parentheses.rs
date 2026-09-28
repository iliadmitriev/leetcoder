impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let mut depth = 0;
        let mut max_depth = 0;

        for ch in s.chars() {
            match ch {
                '(' => depth += 1,
                ')' => depth -= 1,
                _ => {}
            }

            max_depth = max_depth.max(depth);
        }

        max_depth
    }
}
