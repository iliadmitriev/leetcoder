impl Solution {
    pub fn remove_covered_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {
        intervals.sort_by_key(|v| (v[0], -v[1]));

        let mut end = 0;
        let mut count = 0;

        for cur in intervals.iter() {
          if end < cur[1] {
            end = cur[1];
            count += 1;
          }
        }

        count
    }
}