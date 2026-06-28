impl Solution {
    pub fn maximum_element_after_decrementing_and_rearranging(mut arr: Vec<i32>) -> i32 {
       arr.sort();

      let mut prev = 0;

      for &cur in arr.iter() {
          prev = cur.min(prev + 1);
      }

      prev
    }
}