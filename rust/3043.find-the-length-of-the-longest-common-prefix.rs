use std::collections::HashSet;
use std::iter::successors;

impl Solution {
    pub fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let div10 = |n: &i32| if *n >= 10 { Some(*n / 10) } else { None };

        let prefixes: HashSet<i32> = arr1
            .iter()
            .filter(|&&num| num != 0)
            .flat_map(|&num| successors(Some(num), div10))
            .collect();

        arr2.iter()
            .filter_map(|&num| {
                successors(Some(num), div10)
                    .find(|&prefix| prefixes.contains(&prefix))
                    .map(|prefix| (prefix.checked_ilog10().unwrap_or_default() as usize) + 1)
            })
            .max()
            .unwrap_or_default() as i32
    }
}
