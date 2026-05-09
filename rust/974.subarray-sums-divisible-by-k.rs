
impl Solution {
    pub fn subarrays_div_by_k(nums: Vec<i32>, k: i32) -> i32 {
        let mut total = 0;
        let mut cur = 0;
        let mut cache = vec![0; k as usize];

        cache[0] = 1;

        for num in nums {
            cur = (cur + num) % k;
            cur += k;
            cur %= k;

            total += cache[cur as usize];
            cache[cur as usize] += 1;
        }

        return total;
    }
}