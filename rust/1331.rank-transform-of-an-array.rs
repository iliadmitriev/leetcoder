impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        if arr.is_empty() {
          return vec![];
        }

        let n = arr.len();
        let mut s: Vec<_> = arr.iter().copied().enumerate().collect();
        s.sort_by_key(|&(_, x)| x);

        let mut res = vec![0; n];
        let mut prev = s[0].1;
        let mut rank = 1;

        for &(i, v) in s.iter() {
          if prev < v {
            rank += 1;
          }

          res[i] = rank;
          prev = v;
        }

        res
    }
}