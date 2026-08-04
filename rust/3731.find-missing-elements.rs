impl Solution {
    pub fn find_missing_elements(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort_by(|a, b| a.cmp(b));
        let mut prev = nums[0];
        let mut i = 1 as usize;
        let mut res = Vec::<i32>::new();

        while i < nums.len() {
            if prev + 1 != nums[i] {
              res.push(prev + 1);
              prev += 1;
            } else {
              prev = nums[i];
              i += 1;
            }
        }

        return res;
    }
}