use std::collections::VecDeque;
use std::cmp;


impl Solution {
    pub fn can_reach(s: String, min_jump: i32, max_jump: i32) -> bool {
        let n = s.len();

        if (s.chars().last() == Some('1')) {
          return false;
        }

        let min_jump = min_jump as usize;
        let max_jump = max_jump as usize;
        let s = s.as_bytes();

        let mut q: VecDeque<usize> = VecDeque::with_capacity(n);
        let mut seen: usize = 0; // seen values

        q.push_front(0); // start

        while let Some(cur) = q.pop_front() {
            let start = cmp::max(seen, cur + min_jump); // cutoff already seen values
            let end = cmp::min(n, cur + max_jump + 1);  // cutoff array bound

            for nxt in start..end {
              if s[nxt] == b'1' {
                continue
              }

              if nxt == n - 1 {
                return true;
              }

              q.push_back(nxt);
            }

            seen = end;
        }


        false
    }
}