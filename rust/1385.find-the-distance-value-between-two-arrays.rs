use std::collections::HashMap;


impl Solution {
    pub fn find_the_distance_value(arr1: Vec<i32>, arr2: Vec<i32>, d: i32) -> i32 {
        let w = d + 1;
        let mut lo: HashMap<i32, i32> = HashMap::new();
        let mut hi: HashMap<i32, i32> = HashMap::new();

        for &b in arr2.iter() {
            // real true division (fix of Intel's negative number division)
            let k = b.div_euclid(w);

            lo.entry(k)
                .and_modify(|x| *x = (*x).min(b))
                .or_insert(b);

            hi.entry(k)
                .and_modify(|x| *x = (*x).max(b))
                .or_insert(b);
        }

        let far = |a: i32| -> bool {
            let k = a.div_euclid(w);

            !lo.contains_key(&k)
            && hi.get(&(k - 1)).map_or(true, |&x| x < a - d)
            && lo.get(&(k + 1)).map_or(true, |&x| x > a + d)
        };

        arr1.iter().filter(|&&a| far(a)).count() as i32
    }
}