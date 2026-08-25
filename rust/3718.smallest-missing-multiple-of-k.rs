impl Solution {
    pub fn missing_multiple(nums: Vec<i32>, k: i32) -> i32 {
       let n = 5;
       let mut s = vec![0u64; n];

       for n in nums {
        if n % k == 0 {
          let pos = n / k - 1;
          let i = pos / 64;
          let j = pos % 64;

          s[i as usize] |= 1 << j;
        }
       }

       for (i, &v) in s.iter().enumerate() {
          if v == u64::MAX {
            continue;
          }

          let j = (!v).trailing_zeros() as i32;
          let pos = (i as i32) * 64 + j + 1;

          return pos * k;
       }

       k
    }
}