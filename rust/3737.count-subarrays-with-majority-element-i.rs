impl Solution {
    pub fn count_majority_subarrays(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut res = 0;

        let mut pre = n + 1; // running prefix (shifted from [-n;n] to [1; 2*n+1])
        let mut cnt = vec![0; 2 * n + 2]; // count (frequency) prefixes
        let mut acc = vec![0; 2 * n + 2]; // sum of count[k], for all k <= prefix

        cnt[pre] = 1; // prefix = 0
        acc[pre] = 1; 

        for &num in nums.iter() {
            if num == target {
              pre += 1;
            } else {
              pre -= 1;
            }

            cnt[pre] += 1; // update(add) current prefix frequency
            acc[pre] = acc[pre - 1] + cnt[pre]; // update (recalculate) sum of prefix frequencies

            res += acc[pre - 1];
        }

        res
    }
}