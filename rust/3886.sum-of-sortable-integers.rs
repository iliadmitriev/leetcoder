impl Solution {
    pub fn sortable_integers(nums: Vec<i32>) -> i32 {
        let n = nums.len();

        let mut next_descent = vec![n; n];
        for i in (0..n - 1).rev() {
            if nums[i] > nums[i + 1] {
                next_descent[i] = i;
            } else {
                next_descent[i] = next_descent[i + 1];
            }
        }

        let is_sortable = |k: usize| -> bool {
            let mut prev = 0;

            for r in (k - 1..n).step_by(k) {
                let l = r + 1 - k;
                let drop = next_descent[l];

                // case 1: window is a whole piece without a descent (it's sorted)
                if r < drop {
                    // the window left border matches the previous window
                    if prev > nums[l] {
                        return false;
                    }

                    prev = nums[r];
                } else {
                    // case 2: window has at least one descent (drop) within its bounds
                    // can be fixed if (all confitions are met):
                    // * only one drop
                    // * chunks joined into sorted piece
                    // * the new joined piece left border matches the previous window
                    if next_descent[drop + 1] < r || nums[r] > nums[l] || prev > nums[drop + 1] {
                        return false;
                    }

                    prev = nums[drop];
                }
            }

            true
        };

        // factorize `n`
        let mut div = Vec::new();
        for d in (1..).take_while(|d| d * d <= n) {
            if (n % d == 0) {
                div.push(d);

                if (n / d != d) {
                    div.push(n / d);
                }
            }
        }

        let mut res = 0;
        for &d in div.iter() {
            if is_sortable(d) {
                res += d;
            }
        }

        res as i32
    }
}
