impl Solution {
    pub fn first_stable_index(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut vmax = vec![nums[0]; n];
        let mut vmin = vec![nums[n - 1]; n];

        for i in (1..n) {
          vmax[i] = vmax[i - 1].max(nums[i]);
        }

        for i in (0..n-1).rev() {
          vmin[i] = vmin[i + 1].min(nums[i]);
        }

        for i in (0..n) {
          if vmax[i] - vmin[i] <= k {
            return i as i32
          }
        }

        -1
    }
}