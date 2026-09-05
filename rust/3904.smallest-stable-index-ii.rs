impl Solution {
    pub fn first_stable_index(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();

        let mut vmax = nums[0]; // current running max (single value only)
        let mut vmin = vec![nums[n - 1]; n];

        for i in (0..n-1).rev() {
          vmin[i] = vmin[i + 1].min(nums[i]);
        }

        for (i, &x) in nums.iter().enumerate() {
          vmax = vmax.max(x);

          if vmax - vmin[i] <= k {
            return i as i32;
          }
        }

        -1
    }
}