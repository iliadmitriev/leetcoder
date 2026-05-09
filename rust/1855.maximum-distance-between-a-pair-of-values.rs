impl Solution {
    pub fn max_distance(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut maxDist = 0i32;
        let mut i = 0 as usize;

        for (j, &num) in nums2.iter().enumerate() {
          if i >= nums1.len() {
            break;
          }

            if nums1[i as usize] <= num {
              let j = j as i32;
              let i = i as i32;
              
              maxDist = maxDist.max(j - i);
            } else {
              i += 1;
            }
        }

        maxDist
    }
}