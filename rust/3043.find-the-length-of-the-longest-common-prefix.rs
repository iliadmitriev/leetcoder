use std::collections::HashSet;

impl Solution {
    pub fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        Self::longest_common_prefix_slice(&arr1, &arr2)
    }

    pub fn longest_common_prefix_slice(arr1: &[i32], arr2: &[i32]) -> i32 {
        let mut cache = HashSet::new();

        for &num in arr1 {
            let mut n = num;
            while n > 0 {
                cache.insert(n);
                n /= 10;
            }
        }

        let mut max_len = 0;
        for &num in arr2 {
            let mut n = num;
            while n > 0 {
                if cache.contains(&n) {
                    max_len = max_len.max(n.to_string().len() as i32);
                    break;
                }
                n /= 10;
            }
        }

        max_len
    }
}
