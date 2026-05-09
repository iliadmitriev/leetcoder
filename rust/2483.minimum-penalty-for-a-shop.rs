impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let bytes = customers.as_bytes();
        let n = bytes.len();

        let total_penalty = bytes.iter().filter(|&&b| b == b'Y').count() as i32;
        let mut min_penalty = total_penalty;
        let mut current_penalty = total_penalty;
        let mut earliest_hour = 0;

        for (i, &b) in bytes.iter().enumerate() {
            current_penalty += if b == b'N' { 1 } else { -1 };

            if current_penalty < min_penalty {
                min_penalty = current_penalty;
                earliest_hour = i + 1;
            }
        }

        earliest_hour as i32
    }
}