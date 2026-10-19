impl Solution {
    pub fn target_indices(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut less = 0;
        let mut count = 0;
        
        for &num in nums.iter() {
            if num < target {
                less += 1;
            } else if num == target {
                count += 1;
            }
        }
        
        let mut res = Vec::with_capacity(count);
        for num in (less..less+count) {
            res.push(num as i32);
        }
        
        res
    }
}