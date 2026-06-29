impl Solution {
    pub fn num_of_strings(patterns: Vec<String>, word: String) -> i32 {
        let mut res = 0;

        for pat in patterns.iter() {
          if word.contains(pat) {
            res += 1;
          }
        }

        res
    }
}