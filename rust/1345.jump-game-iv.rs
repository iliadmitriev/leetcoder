use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        if n <= 1 {
            return 0;
        }

        let mut adj: HashMap<i32, Vec<usize>> = HashMap::new();
        for (v, &u) in arr.iter().enumerate() {
            adj.entry(u).or_default().push(v);
        }

        let mut seen = vec![false; n];
        let mut queue = VecDeque::with_capacity(n);
        queue.push_back(0);
        seen[0] = true;
        let mut step = 0;

        while !queue.is_empty() {
            let level_size = queue.len();
            for _ in 0..level_size {
                let u = queue.pop_front().unwrap();

                if u == n - 1 {
                    return step;
                }

                if u + 1 < n && !seen[u + 1] {
                    seen[u + 1] = true;
                    queue.push_back(u + 1);
                }

                if u > 0 && !seen[u - 1] {
                    seen[u - 1] = true;
                    queue.push_back(u - 1);
                }

                if let Some(jumps) = adj.remove(&arr[u]) {
                    for j in jumps {
                        if !seen[j] {
                            seen[j] = true;
                            queue.push_back(j);
                        }
                    }
                }
            }

            step += 1
        }

        step
    }
}
