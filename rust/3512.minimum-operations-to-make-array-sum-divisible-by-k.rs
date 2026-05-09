impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        if k == 0 {
            return 0;
        }

        let total = nums.iter().sum::<i32>();

        (k + total % k) % k
    }
}