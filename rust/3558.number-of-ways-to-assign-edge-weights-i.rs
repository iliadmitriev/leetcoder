impl Solution {
    pub fn assign_edge_weights(mut edges: Vec<Vec<i32>>) -> i32 {
      let n = edges.len() + 1; // number of nodes in the tree
      let mut depth = vec![0; n];
      let mut max_depth: i32 = 0;

      edges.sort_by(|a, b| a[0].cmp(&b[0]));

      for e in edges.iter() {
        let (u, v) = (e[0].min(e[1]) - 1, e[0].max(e[1]) - 1);
        depth[v as usize] = 1 + depth[u  as usize];
        max_depth = max_depth.max(depth[v  as usize]);
      }

      let MOD = 1_000_000_007;
      let mut exp: i64 = max_depth as i64 - 1;
      let mut res: i64 = 1;
      let mut base: i64 = 2;

      while exp > 0 {
        if (exp & 1 == 1) {
          res *= base;
          res %= MOD;
        }

        base *= base;
        base %= MOD;
        exp >>= 1;
      }

      res as i32
    }
}