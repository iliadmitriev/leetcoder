impl Solution {
    pub fn find_subtree_sizes(parent: Vec<i32>, s: String) -> Vec<i32> {
        let s = s.as_bytes(); // shadow as 
        let n = parent.len();

        let mut adj = vec![vec![]; n];
        for v in 1..n {
            adj[parent[v] as usize].push(v);
        }

        let mut sizes = vec![1; n];
        let mut last = [-1; 26];

        fn dfs(
            v: usize,
            adj: &[Vec<usize>],
            parent: &[i32],
            s: &[u8],
            sizes: &mut [i32],
            last: &mut [i32; 26],
        ) {
            let label = (s[v] - b'a') as usize;
            let anc = last[label]; // preserve the ancestor for a label

            last[label] = v as i32; // set ancestor for descendant nodes
            for &u in &adj[v] {
                dfs(u, adj, parent, s, sizes, last);
            }
            last[label] = anc; // revert the ancestor for the label

            // drop the root (no ancestor)
            if v == 0 {
                return;
            }

            // appent the result of the current node v
            // to the ancestor of the same label
            // or to the parent
            let p = if anc >= 0 {
                anc as usize
            } else {
                parent[v] as usize
            };

            sizes[p] += sizes[v];
        }

        dfs(0, &adj, &parent, s, &mut sizes, &mut last);

        sizes
    }
}
