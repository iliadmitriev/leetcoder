impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let s = word.as_bytes();
        let mut res = 0;
        let mut lower = vec![false; 26];
        let mut upper = vec![false; 26];

        for &ch in s.iter() {
          if b'a' <= ch && ch <= b'z' {
            lower[(ch - b'a') as usize] = true;
          } else {
            upper[(ch - b'A') as usize] = true;
          }
        }

        for (&a, &b) in lower.iter().zip(upper.iter()) {
          if a && b {
            res += 1;
          }
        }

        res
    }
}