impl Solution {
    pub fn uniform_array(nums1: Vec<i32>) -> bool {
        let mut odd = 0;
        let mut even = 0;
        let mut min_odd = -1;
        let mut min = -1;

        for &v in nums1.iter() {
            if (v & 1) == 1 {
                odd += 1;
                if min_odd == -1 || v < min_odd {
                    min_odd = v;
                }
            } else {
                even += 1;
            }

            if min == -1 || v < min {
                min = v;
            }
        }

        // the array parity is the same (all the number ether even or odd)
        if odd == 0 || even == 0 {
            return true;
        }

        // the array is the mixture of the odd and even numbers
        // in this case we can't make the array all even
        // because, but to make the smallest odd number even by subtraction
        // we need even more smaller number which is impossible
        // therefore, there is only chance to make the array parity odd
        // by subtracting the smallest odd number from all the even
        // but again to comply with the condition (>=1) it should be the smallest one.
        min_odd == min
    }
}