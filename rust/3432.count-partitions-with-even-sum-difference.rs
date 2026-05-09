impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut left = 0;
        let mut right = nums.iter().sum::<i32>();
        let mut counter = 0;

        for i in 0..n - 1 {
            left += nums[i];
            right -= nums[i];

            if (left - right) % 2 == 0 {
                counter += 1;
            }
        }

        counter
    }
}