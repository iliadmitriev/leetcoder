use std::cmp;


impl Solution {
    pub fn min_sum_square_diff(nums1: Vec<i32>, nums2: Vec<i32>, k1: i32, k2: i32) -> i64 {
        let n = nums1.len();
        let mut ops = (k1 as i64) + (k2 as i64);
        let mut mx = 0;
        
        let mut diff_v = Vec::with_capacity(n);
        for i in 0..n {
            let diff = (nums1[i] - nums2[i]).abs() as usize;
            diff_v.push(diff);
            mx = mx.max(diff);
        }

        let mut diff_count = vec![0i64; mx + 1];
        for diff in diff_v {
            diff_count[diff] += 1;
        }

        for diff in (1..=mx).rev() {
            if ops == 0 {
                break;
            }
            let op = cmp::min(ops, diff_count[diff]);

            diff_count[diff] -= op;
            ops -= op;
            diff_count[diff - 1] += op;
        }

        let mut res: i64 = 0;
        for diff in 1..=mx {
            if diff_count[diff] > 0 {
                res += (diff as i64) * (diff as i64) * diff_count[diff];
            }
        }

        res
    }
}
