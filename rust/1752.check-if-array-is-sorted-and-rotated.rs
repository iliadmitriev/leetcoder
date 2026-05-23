impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
       let mut rotations = (nums.first() >= nums.last()) as i32;

       for (prev, cur) in nums.iter().zip(nums.iter().skip(1)) {
          if prev > cur {
            rotations -= 1;
          }

          if rotations < 0 {
            return false;
          }
       }

       true
    }
}