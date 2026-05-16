impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
       let mut lo = 0 as usize;
       let mut hi = nums.len() - 1;
       let mut mid;

       while (lo < hi) {
          mid = (lo + hi) / 2;

          if (nums[mid] > nums[hi]) {
              lo = mid + 1;
          } else if (nums[mid] < nums[hi]) {
              hi = mid;
          } else {
              hi -= 1;
          }
       }

       nums[lo]
    }
}