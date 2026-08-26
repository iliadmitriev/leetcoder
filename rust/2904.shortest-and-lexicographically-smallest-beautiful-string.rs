impl Solution {
    pub fn shortest_beautiful_substring(s: String, k: i32) -> String {
      let b = s.as_bytes();
      let n = s.len();
      let k = k as usize;

      let mut best = n + 1;
      let mut i = 0;
      let mut j = 0;
      let mut l = 0;
      let mut cur = 0;

      for r in 0..n {
        if b[r] == b'1' {
          cur += 1;
        }

        while (l < r && b[l] == b'0') || cur > k {
          if b[l] == b'1' {
            cur -= 1;  
          }

          l += 1;
        }

        if k != cur {
          continue;
        }

        // *********** k == cur window ***********

        let candidate = r + 1 - l;

        if candidate < best {
          (i, j) = (l, r + 1);
          best = candidate;
        } else if candidate == best && &b[l..r+1] < &b[i..j] {
          (i, j) = (l, r + 1);
        }
      }

      s[i..j].to_string()
    }
}