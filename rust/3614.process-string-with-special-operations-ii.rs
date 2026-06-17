impl Solution {
    pub fn process_str(s: String, k: i64) -> char {
        let mut k = k;
        let mut size = 0 as i64;

        for ch in s.chars() {
            match ch {
                // remove
                '*' => {
                    size = (size - 1).max(0);
                }
                // duplicate
                '#' => {
                    size *= 2;
                }
                // reverse
                '%' => {} // length not changed
                // add char
                _ => {
                    size += 1;
                }
            }
        }

        if k >= size {
            return '.';
        }

        for ch in s.chars().rev() {
            match ch {
                // inverse remove
                '*' => {
                    size += 1;
                }
                // inverse duplicate
                '#' => {
                    let half = size / 2;
                    if k >= half {
                        // only affect if is in 2nd half
                        k -= half; // shift indices
                    }
                    size = half;
                }
                // inverse reverse
                '%' => {
                    k = size - 1 - k; // reverse indexation
                }
                // inverse add char
                _ => {
                    if k == size - 1 {
                        return ch; // char is k-th
                    }

                    size -= 1;
                }
            }
        }

        '.' // default
    }
}
