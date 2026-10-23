impl Solution {
    pub fn sort_permutation(nums: Vec<i32>) -> i32 {
        let mut res = -1;

        for (i, &num) in nums.iter().enumerate() {
            if i as i32 == num {
                continue;
            }

            res &= num;
        }

        res.max(0)
    }
}