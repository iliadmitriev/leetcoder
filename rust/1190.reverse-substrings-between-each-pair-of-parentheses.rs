impl Solution {
    pub fn reverse_parentheses(s: String) -> String {
       let s: Vec<char> = s.chars().collect();
       let n = s.len();

       let mut pairs = vec![0; n];
       let mut stack = Vec::new();

       for i in 0..n {
        match s[i] {
          '(' => stack.push(i),
          ')' => {
            if let Some(pair) = stack.pop() {
              pairs[pair] = i;
              pairs[i] = pair;
            }
          },
          _ => {},
        }
      }

      let mut res = Vec::with_capacity(n);
      let mut i = 0; // current index
      let mut fwd = true; // direction toggle

      while i < n {
        match s[i] {
          '(' | ')' => {
            i = pairs[i]; // teleport
            fwd = !fwd; // flip direction
          }
          ch => {
            res.push(ch);
          }
        }

        if fwd {
          i += 1;
        } else {
          i -= 1;
        }
      }

      res.iter().collect()
    }
}