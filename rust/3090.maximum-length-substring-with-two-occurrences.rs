impl Solution {
    pub fn maximum_length_substring(s: String) -> i32 {
        let s = s.into_bytes();
        let mut win = vec![0; 26];
        let mut j = 0;
        let mut largest = 0;
        
        for (i, ch) in s.iter().enumerate() {
          let r = (ch - b'a') as usize;
          win[r] += 1;

          while (win[r] > 2) {
            let l = (s[j] - b'a') as usize;
            win[l] -= 1;
            j += 1;
          }

          largest = largest.max(i - j + 1);
        }

        largest as i32
    }
}