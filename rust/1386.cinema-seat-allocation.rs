use std::collections::HashMap;

impl Solution {
    pub fn max_number_of_families(n: i32, reserved_seats: Vec<Vec<i32>>) -> i32 {
        // . - unused, 1 - set, 0 - unset
        let m1 = 0x0Fu8; // . 0000 1111 .
        let m2 = 0xF0u8; // . 1111 0000 .
        let m3 = 0x3Cu8; // . 0011 1100 .

        let mut rows: HashMap<i32, u8> = HashMap::new();

        for seat in &reserved_seats {
          let i = seat[0];
          let j = seat[1] - 2;

          if j < 0 || j > 7 {
            continue;
          }

          let mut en = rows.entry(i).or_default();
          *en |= 1 << j; 
        }

        // optimally all empy rows can be filled
        // with the two quad seats
        let mut total = (n - rows.len() as i32) * 2;

        for row in rows.values() {
            if row & m1 == 0 || row & m2 == 0 || row & m3 == 0 {
              total += 1;
            }
        }

        total
    }
}