
use std::collections::HashMap;

impl Solution {
    pub fn count_covered_buildings(_n: i32, buildings: Vec<Vec<i32>>) -> i32 {
        let mut by_x: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut by_y: HashMap<i32, Vec<i32>> = HashMap::new();

        // Group coordinates
        for building in &buildings {
            let (x, y) = (building[0], building[1]);
            by_x.entry(x).or_default().push(y);
            by_y.entry(y).or_default().push(x);
        }

        // Sort all lists
        by_x.values_mut().for_each(|ys| ys.sort_unstable());
        by_y.values_mut().for_each(|xs| xs.sort_unstable());

        let mut covered = 0;

        for (&x, ys) in &by_x {
            // Skip lines with fewer than 3 points — no "middle" point possible
            if ys.len() < 3 {
                continue;
            }

            // Check only interior points (indices 1 to len-2)
            for &y in &ys[1..ys.len() - 1] {
                let xs_on_same_y = &by_y[&y];
                if xs_on_same_y.first() < Some(&x) && Some(&x) < xs_on_same_y.last() {
                    covered += 1;
                }
            }
        }

        covered
    }
}
