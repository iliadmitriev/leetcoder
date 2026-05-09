
use std::collections::HashMap;

impl Solution {
    pub fn special_triplets(nums: Vec<i32>) -> i32 {
        let MOD: i64 = 1_000_000_007;
        let mut total: i64 = 0;

        let mut cache = nums
            .iter()
            .enumerate()
            .fold(HashMap::new(), |mut cache, (i, &num)| {
                cache.entry(num).or_insert(Vec::new()).push(i);
                cache
            });

        if let Some(v) = cache.get(&0) {
            let n = v.len() as i64;

            // C(n, 3) = n! / (3! * (n - 3)!)
            // C(n, 3) = n * (n - 1) * (n - 2) / 6
            total += n * (n - 1) * (n - 2) / 6;
            total %= MOD;

            cache.remove(&0);
        }

        for (num, indices) in cache.iter() {
            let x2 = num * 2;

            if let Some(idx2) = cache.get(&x2) {
                for &idx in indices.iter() {
                    let left = match idx2.binary_search(&(idx + 1)) {
                        Ok(left) => left,
                        Err(left) => left,
                    } as i64;

                    let right = idx2.len() as i64
                        - match idx2.binary_search(&idx) {
                            Ok(right) => right,
                            Err(right) => right,
                        } as i64;

                    total += left * right;
                    total %= MOD;
                }
            }
        }

        total as i32
    }
}