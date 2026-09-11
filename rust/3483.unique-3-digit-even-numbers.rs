impl Solution {
    pub fn total_numbers(digits: Vec<i32>) -> i32 {
        let mut total = 0;
        let mut cnt = [0; 10];

        for n in digits {
          cnt[n as usize] += 1;
        }

        for c in (1..10) {
          if cnt[c] == 0 {
            continue;
          }

          cnt[c] -= 1;

          for d in (0..10) {
            if cnt[d] == 0 {
              continue;
            }

            cnt[d] -= 1;

            for u in (0..10).step_by(2) {
              if cnt[u] == 0 {
                continue;
              }

              total += 1;
            }

            cnt[d] += 1;
          }

          cnt[c] += 1;
        } 

        total   
    }
}