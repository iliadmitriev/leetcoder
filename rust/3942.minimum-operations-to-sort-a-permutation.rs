use std::cmp;

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();

        if n <= 1 {
            return 0;
        }

        let shift = nums
            .iter()
            .position(|&x| x == 0)
            .expect("there must be a zero in the given permutation array");

        let mut asc = true;
        let mut desc = true;

        for num in (1..n) {
            let i = (num + shift) % n; // position of num

            if nums[i] != num as i32 {
                asc = false;
            }

            if nums[i] != (n - num) as i32 {
                desc = false;
            }

            if !asc && !desc {
                return -1;
            }
        }

        (match asc {
            true => cmp::min(shift, n - shift + 2),
            false => cmp::min(n - shift, shift + 2),
        }) as i32
    }
}
