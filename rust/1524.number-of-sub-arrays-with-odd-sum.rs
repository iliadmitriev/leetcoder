impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>) -> i32 {
        let mut odd = 0 as i64;
        let mut even = 0 as i64;
        let MMOD = 1_000_000_007 as i64;
        
        for &num in arr.iter() {
            if num % 2 == 1 {
                let odd_prev = odd;
                odd = even + 1;
                even = odd_prev;
            } else {
                even += 1;
            }
        }
        
        (odd * (even + 1) % MMOD) as i32
    }
}