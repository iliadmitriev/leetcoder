
use std::cmp;

impl Solution {
    fn day_of_year(s: &str) -> i32 {
        const MONTHS: [i32; 13] = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
        
        let m: usize = s[0..2].parse().unwrap_or(0);
        let d: i32 = s[3..5].parse().unwrap_or(0);
        
        MONTHS[m] + d
    }
    
    pub fn count_days_together(arrive_alice: String, leave_alice: String, arrive_bob: String, leave_bob: String) -> i32 {
        let arrive = cmp::max(Self::day_of_year(&arrive_alice), Self::day_of_year(&arrive_bob));
        let leave = cmp::min(Self::day_of_year(&leave_alice), Self::day_of_year(&leave_bob));
        
        cmp::max(0, leave - arrive + 1)
    }
}