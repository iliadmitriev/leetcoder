impl Solution {
    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool> {
        let n = nums.len();
        let mut res: Vec<bool> = Vec::with_capacity(n);
        let mut cur = 0;

        for num in nums {
            cur <<= 1;
            cur |= num;
            cur %= 5;

            res.push(cur == 0);
        }

        res
    }
}