use  std::collections::HashSet;


impl Solution {
    pub fn missing_integer(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut i = 1 as usize;
        let mut pre = nums[0];
        let uniq = nums.iter().copied().collect::<HashSet<_>>();

        while i < n && nums[i - 1] + 1 == nums[i] {
          pre += nums[i];
          i += 1;
        }

        while uniq.contains(&pre) {
          pre += 1;
        } 

        return pre;
    }
}