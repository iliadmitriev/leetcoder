use std::cmp;

impl Solution {
    pub fn longest_valid_parentheses(s: String) -> i32 {
        fn scan(seq: impl Iterator<Item = char>, op: char) -> i32 {
            let mut res = 0;
            let mut opening = 0;
            let mut closing = 0;

            for ch in seq {
                if ch == op {
                    opening += 1;
                } else {
                    closing += 1;
                }

                if opening == closing {
                    res = res.max(opening + closing);
                }

                if opening < closing {
                    opening = 0;
                    closing = 0;
                }
            }

            res
        }

        cmp::max(scan(s.chars(), '('), scan(s.chars().rev(), ')'))
    }
}
