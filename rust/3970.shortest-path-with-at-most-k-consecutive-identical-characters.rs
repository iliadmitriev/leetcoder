use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn shortest_path(n: i32, edges: Vec<Vec<i32>>, labels: String, k: i32) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let labels = labels.as_bytes();

        let mut g = vec![vec![]; n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2] as usize;

            g[u].push((v, w));
        }

        // heap of tuples {distance, node, streak}
        let mut h: BinaryHeap<Reverse<(usize, usize, usize)>> = BinaryHeap::new();
        // path[node][streak] = distance
        let mut path = vec![vec![usize::MAX; k + 1]; n];

        // start from node 0 with 0 distance and streak of 1 symbol
        h.push(Reverse((0, 0, 1)));
        path[0][1] = 0;

        while let (Some(Reverse((dist, node, streak)))) = h.pop() {
            if dist > path[node][streak] {
                continue;
            }

            if node == n - 1 {
                return dist as i32;
            }

            for &(nnode, weight) in g[node].iter() {
                let nstreak = if labels[node] == labels[nnode] {
                    streak + 1
                } else {
                    1
                };

                if nstreak > k {
                    continue;
                }

                let ndist = dist + weight;
                if ndist >= path[nnode][nstreak] {
                    continue;
                }

                path[nnode][nstreak] = ndist;
                h.push(Reverse((ndist, nnode, nstreak)));
            }
        }

        -1
    }
}
