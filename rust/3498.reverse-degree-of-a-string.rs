impl Solution {
    pub fn reverse_degree(s: String) -> i32 {
        let base = b'a' as i32 + 26;

        s.bytes()
            .enumerate()
            .map(|(i, ch)| (base - ch as i32) * (i + 1) as i32)
            .sum()
    }
}
