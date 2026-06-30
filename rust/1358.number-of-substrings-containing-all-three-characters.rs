impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        let n = s.len();

        let mut count = 0;
        let mut win = vec![0, 0, 0];

        let mut l = 0 as usize;

        for (r, ch) in s.bytes().enumerate() {
          let right = (ch - b'a') as usize;

          win[right] += 1;

          while win[0] > 0 && win[1] > 0 && win[2] > 0 {
            count += (n - r) as i32; // add rest right part l times

            let left = (s.as_bytes()[l] - b'a') as usize;

            win[left] -= 1;
            l += 1;
          }
        }

        count
    }
}