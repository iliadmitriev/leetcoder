impl Solution {
    pub fn min_insertions(s: String) -> i32 {
        let mut closing_needed = 0;
        let mut res = 0;

        for ch in s.chars() {
            match ch {
                '(' => {
                    closing_needed += 2;

                    if closing_needed % 2 == 1 {
                        res += 1;
                        closing_needed -= 1;
                    }
                }
                ')' => {
                    closing_needed -= 1;

                    if closing_needed < 0 {
                        res += 1;
                        closing_needed += 2;
                    }
                }
                _ => unreachable!(),
            }
        }

        res + closing_needed
    }
}
