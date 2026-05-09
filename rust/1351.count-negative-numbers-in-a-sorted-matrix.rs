impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len() as i32;
        let n = grid.first().unwrap().len() as i32;

        let mut cur = n;

        grid.iter()
            .map(|row| {
                cur = Self::zero_pos(row, 0, cur);

                n - cur
            })
            .sum()
    }

    fn zero_pos(arr: &Vec<i32>, lo: i32, hi: i32) -> i32 {
        let mut l = lo;
        let mut r = hi;

        // let mut mid: i32;
        //
        // while (l < r) {
        //     mid = (l + r) / 2;
        //
        //     if arr[mid as usize] >= 0 {
        //         l = mid + 1
        //     } else {
        //         r = mid
        //     }
        // }
        //
        // return l;

        while l < r {
            if arr[(r - 1) as usize] >= 0 {
                return r;
            }

            r -= 1;
        }

        0
    }
}