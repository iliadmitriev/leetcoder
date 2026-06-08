impl Solution {
    pub fn pivot_array(nums: Vec<i32>, pivot: i32) -> Vec<i32> {
        let less = nums.iter().copied().filter(|&x| x < pivot);

        let equal = nums.iter().copied().filter(|&x| x == pivot);

        let greater = nums.iter().copied().filter(|&x| x > pivot);

        less.chain(equal).chain(greater).collect()
    }
}
