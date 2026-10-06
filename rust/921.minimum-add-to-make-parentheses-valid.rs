impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let mut opened = 0;
        let mut closed = 0;

        for ch in s.chars() {
            match ch {
                '(' => {
                    opened += 1;
                },
                ')' => {
                    if opened > 0 {
                        opened -= 1;
                    } else {
                        closed += 1;
                    }
                },
                _ => unreachable!(),
            }
        }

        opened + closed
    }
}
