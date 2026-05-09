impl Solution {
    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let max1 = *nums1.iter().max().unwrap_or(&0);
        let min2 = *nums2.iter().min().unwrap_or(&0);

        if max1 < 0 && min2 > 0 {
            return max1 * min2;
        }

        let min1 = *nums1.iter().min().unwrap_or(&0);
        let max2 = *nums2.iter().max().unwrap_or(&0);

        if min1 > 0 && max2 < 0 {
            return min1 * max2;
        }

        let m = nums1.len();
        let n = nums2.len();

        let mut next_row = vec![0; n + 1]; // (i + 1)-th row
        let mut curr_row = vec![0; n + 1]; // i-th row

        for i in (0..m).rev() {
            for j in (0..n).rev() {
                let take = nums1[i] * nums2[j] + next_row[j + 1];
                let skip1 = next_row[j];
                let skip2 = curr_row[j + 1];

                curr_row[j] = take.max(skip1).max(skip2);
            }

            std::mem::swap(&mut curr_row, &mut next_row);
        }

        next_row[0]
    }
}