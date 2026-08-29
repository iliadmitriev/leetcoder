impl Solution {
    pub fn lexicographically_smallest_array(nums: Vec<i32>, limit: i32) -> Vec<i32> {
        let n = nums.len();
        if n == 0 {
            return Vec::new();
        }

        // sorted vec of pairs {(position, value), ...}
        let mut data: Vec<(usize, i32)> = nums.into_iter().enumerate().collect();
        data.sort_by_key(|&(_, v)| v);

        let mut result = vec![-1; n]; // result
        let mut start = 0; // start index of the current group in data

        for i in 1..n {
            // if gap is greater than limit: add sorted numbers to result and start a new group
            if data[i].1 - data[i - 1].1 > limit {
                Self::assign_group(&data, &mut result, start, i);

                start = i; // start a new group
            }
        }

        Self::assign_group(&data, &mut result, start, n);

        result
    }

    fn assign_group(data: &[(usize, i32)], result: &mut [i32], start: usize, end: usize) {
        // take all the indices in the current group and sort them ascending
        let mut indices: Vec<usize> = data[start..end].iter().map(|&(idx, _)| idx).collect();
        indices.sort_unstable();

        // add data according to the sorted indices
        for (k, &j) in indices.iter().enumerate() {
            result[j] = data[start + k].1;
        }
    }
}
