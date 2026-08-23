impl Solution {
    pub fn sum_game(num: String) -> bool {
        let num = num.as_bytes();
        
        let collect = |l: usize, r: usize| -> (i32, i32) {
            let mut n = 0;
            let mut q = 0;

            for k in (l..r) {
              if num[k] == b'?' {
                q += 1;
              } else {
                n += (num[k] - b'0') as i32;
              }
            }

            (n, q)
        };

        let n = num.len();
        let (n0, q0) = collect(0, n / 2);
        let (n1, q1) = collect(n / 2, n);

        (q0 + q1) % 2 == 1 || n0 - n1 != (q1 - q0) * 9 / 2
    }
}