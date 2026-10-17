impl Solution {
    pub fn min_swaps(nums: Vec<i32>) -> i32 {
        let digits = |mut x: i32| -> i32 {
            let mut y = 0;
            while (x > 0) {
                y += x % 10;
                x /= 10;
            }

            y
        };

        let n = nums.len();
        let mut arr: Vec<(i32, i32, usize)> = Vec::with_capacity(n); // S: O(n)
        let mut vis = vec![false; n]; // S: O(n)

        for (i, &x) in nums.iter().enumerate() {
            arr.push((digits(x), x, i));
        }

        arr.sort(); // T: O(n log n)
        let mut swaps = 0;

        for i in (0..n) {
            // if this cycle is fixed already or the num is at the proper position -> skip
            if vis[i] || i == arr[i].2 {
                continue;
            }

            let mut j = i;
            let mut cycle = 0; // number of swaps in current cycle

            while !vis[j] {
                vis[j] = true;
                j = arr[j].2;
                cycle += 1;
            }

            swaps += cycle - 1;
        }

        swaps
    }
}
