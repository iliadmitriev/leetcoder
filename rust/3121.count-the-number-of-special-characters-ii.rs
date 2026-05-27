impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let alpha = 26;
        let mut lower = vec![None; alpha];
        let mut upper = vec![None; alpha];

        for (i, ch) in word.bytes().enumerate() {
            if ch >= b'a' {
                lower[(ch - b'a') as usize] = Some(i);
            } else if upper[(ch - b'A') as usize].is_none() {
                upper[(ch - b'A') as usize] = Some(i);
            }
        }

        lower
            .iter()
            .zip(upper.iter())
            .filter(|(a, b)| {
              match (a, b) {
                (Some(a), Some(b)) => a < b,
                _ => false,
              }
            })
            .count() as i32
    }
}
