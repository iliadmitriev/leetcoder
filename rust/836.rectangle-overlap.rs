use std::cmp;


impl Solution {
    pub fn is_rectangle_overlap(rec1: Vec<i32>, rec2: Vec<i32>) -> bool {
      let [xa1, ya1, xa2, ya2] = rec1.as_slice().try_into().expect("Expected 4 elements");
      let [xb1, yb1, xb2, yb2] = rec2.as_slice().try_into().expect("Expected 4 elements");

      
       let (x1, y1) = (cmp::max(xa1, xb1), cmp::max(ya1, yb1));
       let (x2, y2) = (cmp::min(xa2, xb2), cmp::min(ya2, yb2));
      
        x1 < x2 && y1 < y2
    }
}