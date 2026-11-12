impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let mut inc = 1;
        let mut dec = 1;
        let mut longest = 1;
        
        for i in (1..nums.len()) {
            if nums[i-1] < nums[i] {
                inc += 1;
                dec = 1;
            } else if nums[i-1] > nums[i] {
                inc = 1;
                dec += 1;
            } else {
                inc = 1;
                dec = 1;
            }
            
            longest = longest.max(inc);
            longest = longest.max(dec);
        }
        
        longest
    }
}