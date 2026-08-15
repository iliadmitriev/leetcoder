impl Solution {
    pub fn longest_subsequence(nums: Vec<i32>) -> i32 {
        let size = nums.len() as i32;
        let all = nums.iter().fold(0, |acc, x| acc ^ x);

        if all != 0 {
          return size;
        }

        let non_zero = nums.iter().filter(|&&x| x != 0 ).count();

        if non_zero != 0 {
          return size - 1;
        }

        0 
    }
}