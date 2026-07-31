impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        let N = 26 as usize;
        let mut count = 0;
        let mut step = 0;
        let mut cnt = vec![0; N];

        for ch in word.bytes() {
          cnt[(ch - b'a') as usize] += 1;
        }

        cnt.sort_by(|a, b| b.cmp(a)); // reverse sort

        for (i, c) in cnt.iter().enumerate() {
          if i % 8 == 0 {
            step += 1;
          }

          count += c * step;
        }

        count
    }
}