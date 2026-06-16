impl Solution {
    pub fn process_str(s: String) -> String {
        let mut res = Vec::new();

        for ch in s.chars() {
            match ch {
                '*' => {
                    res.pop();
                }
                '#' => {
                    res.extend_from_within(..);
                }
                '%' => {
                    res.reverse();
                }
                _ => {
                    res.push(ch);
                }
            }
        }

        res.into_iter().collect()
    }
}
