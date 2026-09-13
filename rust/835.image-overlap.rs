use std::collections::HashMap;

impl Solution {
    pub fn largest_overlap(img1: Vec<Vec<i32>>, img2: Vec<Vec<i32>>) -> i32 {
       let n = img1.len();

       let mut ones1: Vec<usize> = Vec::new();
       let mut ones2: Vec<usize> = Vec::new();

       // key pack: row << shift | col
       // values range in [0; 60]
       // at most 6 bits needed to store values up to 64
       let shift = 6; // row bits shift
       let mask = (1 << shift) - 1; // column mask

        for i in (0..n) {
          for j in (0..n) {
            if img1[i][j] == 1 {
              ones1.push(i << shift | j)
            }

            if img2[i][j] == 1 {
              ones2.push(i << shift | j);
            }
          }
        }

        // count frequencies of all the possible poinst cross diffrence
        let mut freq: HashMap<usize, i32> = HashMap::new();
        for &rc1 in ones1.iter() {
          for &rc2 in ones2.iter() {
            let (r1, c1) = (rc1 >> shift, rc1 & mask);
            let (r2, c2) = (rc2 >> shift, rc2 & mask);

            let key = ((n + r2 - r1) << shift) | (n + c2 - c1);
            let count = freq.entry(key).or_insert(0);
            *count += 1;
          }
        }

        *freq.values().max().unwrap_or(&0)
    }
}