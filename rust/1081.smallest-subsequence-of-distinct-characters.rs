impl Solution {
    pub fn smallest_subsequence(s: String) -> String {
        let M = 26;

        let idx = |c: char| { (c as usize) - ('a' as usize) };

        let mut cnt = vec![0; M];
        let mut added = vec![false; M];
        let mut st = Vec::with_capacity(M);

        for ch in s.chars() {
          cnt[idx(ch)] += 1;
        }

        for ch in s.chars() {
          cnt[idx(ch)] -= 1; // reduce number of characters left (for future replacements)

          // if current char is on the stack (for now), skip it
          if added[idx(ch)] {
            continue;
          }

          // if the current char is lexicographically smaller then the character on top of the stack
          // and it can be replaced in the future (still have this chracters left)
          // then drop it now, and for a future replacement
          while let Some(&top) = st.last() && top > ch && cnt[idx(top)] > 0 {
            st.pop();
            added[idx(top)] = false;
          }

          st.push(ch);
          added[idx(ch)] = true;
        }

        st.iter().collect()
    }
}