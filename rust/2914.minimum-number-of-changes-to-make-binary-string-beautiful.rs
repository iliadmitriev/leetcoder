impl Solution {
    pub fn min_changes(s: String) -> i32 {
        let mut count = 0;
        let s = s.as_bytes();
        let n = s.len();
        
        for i in (0..n).step_by(2) {
            if s[i] != s[i + 1] {
                count += 1;
            }
        }
        
        count
    }
}