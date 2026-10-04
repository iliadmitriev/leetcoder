use std::cmp;

impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let mut opening_min = 0;
        let mut opening_max = 0;
        
        for ch in s.chars() {
            match ch {
                '(' => {
                    opening_min += 1;
                    opening_max += 1;
                },
                ')' => {
                    opening_min = (0).max(opening_min - 1);
                    opening_max -= 1
                },
                '*' => {
                    opening_min = (0).max(opening_min - 1);
                    opening_max += 1
                },
                _ => unreachable!(),
            }
            
            if opening_max < 0 {
                return false;
            }
        }
        
        opening_min == 0
    }
}