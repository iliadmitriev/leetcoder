use std::collections::HashMap;

impl Solution {
    pub fn max_number_of_balloons(text: String) -> i32 {
        let mut counts = [0; 26];
        for ch in text.bytes() {
          counts[(ch - b'a') as usize] += 1;
        }

        let b = counts[(b'b' - b'a') as usize];
        let a = counts[(b'a' - b'a') as usize];
        let ll = counts[(b'l' - b'a') as usize] / 2;
        let oo = counts[(b'o' - b'a') as usize] / 2;
        let n = counts[(b'n' - b'a') as usize];

        [b, a, ll, oo, n].into_iter().min().unwrap_or(0)

        // let count = text
        //   .chars()
        //   .fold(HashMap::new(), |mut map, ch| {
        //     *map.entry(ch).or_insert(0) += 1;
        //     map
        //   });
        
        // let mut res = text.len() as i32;

        // res = res.min(*count.get(&'b').unwrap_or(&0));
        // res = res.min(*count.get(&'a').unwrap_or(&0));
        // res = res.min(*count.get(&'l').unwrap_or(&0) / 2);
        // res = res.min(*count.get(&'o').unwrap_or(&0) / 2);
        // res = res.min(*count.get(&'n').unwrap_or(&0));

        // res
    }
}