impl Solution {
    pub fn map_word_weights(words: Vec<String>, weights: Vec<i32>) -> String {
        let n = 26;
        let a = b'a' as u32;
        words
            .into_iter()
            .map(|w| {
                let s = w
                    .bytes()
                    .map(|b| weights[(b - b'a') as usize] as u32)
                    .sum::<u32>();
                (b'z' - (s % 26) as u8) as char
            })
            .collect::<String>()
    }
}
