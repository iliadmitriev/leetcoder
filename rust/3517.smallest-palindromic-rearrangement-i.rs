impl Solution {
    pub fn smallest_palindrome(s: String) -> String {
        let mut cnt = [0; 26];
        let n = s.len();
        let mid = n / 2;
        let bytes = s.as_bytes();

        let mut res = vec![0u8; n];
        let mut i = 0;

        // Count characters in the first half (excluding the middle)
        for idx in 0..mid {
            cnt[(bytes[idx] - b'a') as usize] += 1;
        }

        // Fill left half with characters in ascending order
        for j in 0..26 {
            let cur = b'a' + j as u8;
            for _ in 0..cnt[j] {
                res[i] = cur;
                i += 1;
            }
        }

        // Insert middle character if length is odd
        if n % 2 == 1 {
            res[i] = bytes[mid];
            i += 1;
        }

        // Fill right half with characters in descending order (mirror)
        for j in (0..26).rev() {
            let cur = b'a' + j as u8;
            for _ in 0..cnt[j] {
                res[i] = cur;
                i += 1;
            }
        }

        // Convert bytes to String (safe because input is ASCII)
        String::from_utf8(res).expect("valid UTF-8")
    }
}