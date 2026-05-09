
use std::collections::HashMap;

impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;

        // count the frequency of points on each line parallel to x
        let mut line_counts = HashMap::new();
        for point in &points {
            *line_counts.entry(point[1]).or_insert(0) += 1;
        }

        let mut res: i64 = 0;
        let mut total: i64 = 0;

        for &count in line_counts.values() {
            let edges = count * (count - 1) / 2;

            res += total * edges;
            res %= MOD;

            total += edges;
            total %= MOD;
        }

        res as i32
    }
}