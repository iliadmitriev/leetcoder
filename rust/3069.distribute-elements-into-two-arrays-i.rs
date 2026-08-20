impl Solution {
    pub fn result_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut arr1 = Vec::with_capacity(n);
        let mut arr2 = Vec::new();

        arr1.push(nums[0]);
        arr2.push(nums[1]);

        for i in (2..n) {
          if arr1.last().unwrap_or(&i32::MIN) > arr2.last().unwrap_or(&i32::MIN) {
            arr1.push(nums[i]);
          } else {
            arr2.push(nums[i]);
          }
        }

        arr1.extend(arr2);

        arr1
    }
}