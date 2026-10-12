impl Solution {
    pub fn max_sum(nums: Vec<i32>, k: i32) -> i32 {
        let size = 30;
        let md = 1000000007 as i64;

        let mut res = 0 as i64;
        let mut bits = vec![0; size];

        for num in nums.iter() {
            for i in (0..size) {
                if num & (1 << i) > 0 {
                    bits[i] += 1;
                }
            }
        }

        for _ in (0..k) {
            let mut v = 0 as i64;
            for i in (0..size).rev() {
                if bits[i] > 0 {
                    bits[i] -= 1;
                    v |= 1 << i;
                }
            }

            res = (res + v * v) % md;
        }

        res as i32
    }
}
