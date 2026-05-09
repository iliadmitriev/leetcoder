impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let rows = strs.len();
        let cols = strs.first().unwrap().len();

        let mut removed = 0;
        let mut in_order = vec![false; rows];

        (0..cols).into_iter().for_each(|c| {
            let mut broken = false;
            for r in 1..rows {
                if in_order[r] {
                    continue;
                }

                if strs[r - 1].as_bytes()[c] > strs[r].as_bytes()[c] {
                    broken = true;
                    break;
                }
            }

            if broken {
                removed += 1;
                return;
            }

            for r in 1..rows {
                if !in_order[r] && strs[r - 1].as_bytes()[c] < strs[r].as_bytes()[c] {
                    in_order[r] = true;
                }
            }
        });

        removed
    }
}