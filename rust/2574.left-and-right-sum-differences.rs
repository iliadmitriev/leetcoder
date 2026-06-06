impl Solution {
    pub fn left_right_difference(nums: Vec<i32>) -> Vec<i32> {
        let total: i32 = nums.iter().sum();

        nums
          .into_iter()
          .scan(0, move |left, cur| {
            let right = total - *left - cur;
            let diff = (*left - right).abs();

            *left += cur;
            Some(diff)
          })
          .collect()
    }
}