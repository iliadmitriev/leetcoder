impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32 {
      let total = nums.iter().sum::<i32>();
      let target = total - x;
      let n = nums.len();

      if target < 0 {
        return -1;
      }

      if target == 0 {
        return n as i32;
      }

      let mut res = n + 1;
      let mut cur = 0;
      let mut l = 0;

      for (r, &num) in nums.iter().enumerate() {
        cur += num;

        while l <= r && cur > target {
          cur -= nums[l];
          l += 1;
        }

        if cur == target {
          res = res.min(n - r + l - 1);
        }
      }

      if res > n {
        return -1;
      }

      res as i32
    }
}