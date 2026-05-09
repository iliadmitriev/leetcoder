
impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        const INF: i64 = 1e15 as i64;

        let mut prefix = vec![INF; k as usize];
        prefix[(k - 1) as usize] = 0;

        let mut res: i64 = -INF;
        let mut cur: i64 = 0;

        for (i, &num) in nums.iter().enumerate() {
            cur += num as i64;
            let idx = i % k as usize;
            let old = prefix[idx];

            prefix[idx] = old.min(cur);
            res = res.max(cur - old);
        }

        res
    }
}