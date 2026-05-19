use std::cmp::Ordering;


impl Solution {
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut it1 = nums1.iter().peekable();
        let mut it2 = nums2.iter().peekable();

        while let (Some(&a), Some(&b)) = (it1.peek(), it2.peek()) {
            match a.cmp(b) {
                Ordering::Less => it1.next(),
                Ordering::Greater => it2.next(),
                Ordering::Equal => return *a,
            };
        }

        return -1;
    }
}
