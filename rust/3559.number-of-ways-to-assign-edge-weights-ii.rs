struct BinaryLiftTree {
    size: usize,
    log_size: usize,
    depth: Vec<usize>,
    adj: Vec<Vec<usize>>,
    up: Vec<Vec<usize>>,
}

impl BinaryLiftTree {
    pub fn new(size: usize) -> Self {
        let log_size = size.checked_ilog2().map_or(0, |v| v + 1) as usize;

        Self {
            size: size,
            log_size: log_size,
            depth: vec![0; size],
            adj: vec![vec![]; size],
            up: vec![vec![0; log_size]; size],
        }
    }

    pub fn add_edge(&mut self, u: usize, v: usize) {
        let (mut u, mut v) = (u, v);
        if u > v {
            (u, v) = (v, u);
        }

        self.adj[u].push(v);
    }

    fn dfs(&mut self, u: usize, p: usize, d: usize) {
        self.depth[u] = d;
        self.up[u][0] = p;

        for j in (1..self.log_size) {
            if self.up[u][j - 1] != 0 {
                let w = self.up[u][j - 1];
                self.up[u][j] = self.up[w][j - 1];
            } else {
                break;
            }
        }

        let num_children = self.adj[u].len();
        for i in 0..num_children {
            let v = self.adj[u][i];

            if v == p {
                continue;
            }

            self.dfs(v, u, d + 1);
        }
    }

    pub fn preprocess(&mut self, root: usize) {
        self.dfs(root, 0, 0);
    }

    pub fn kth_ancestor(&self, mut u: usize, k: usize) -> usize {
        for j in (0..self.log_size) {
            if (k >> j) & 1 == 1 {
                u = self.up[u][j] as usize;
            }

            if u == 0 {
                return 0;
            }
        }

        u
    }

    pub fn get_lca(&self, u: usize, v: usize) -> usize {
        let (mut u, mut v) = (u, v);
        if self.depth[u] < self.depth[v] {
            (u, v) = (v, u)
        }

        let diff = self.depth[u] - self.depth[v];

        u = self.kth_ancestor(u, diff as usize);

        if u == v {
            return u;
        }

        for j in (0..self.log_size).rev() {
            if self.up[u][j] != self.up[v][j] {
                u = self.up[u][j];
                v = self.up[v][j];
            }
        }

        self.up[u][0]
    }

    pub fn get_distance(&self, u: usize, v: usize) -> i32 {
        let common = self.get_lca(u, v);
        let dist = self.depth[u] + self.depth[v] - 2 * self.depth[common];

        dist as i32
    }
}

impl Solution {
    fn bin_mod_exp(exp: i32) -> i32 {
        if exp < 0 {
            return 0;
        }

        let MOD = 1_000_000_007 as u64;
        let mut res = 1 as u64;
        let mut base = 2 as u64;
        let mut exp = exp as u64;

        while exp > 0 {
            if exp & 1 == 1 {
                res *= base;
                res %= MOD
            }

            base *= base;
            base %= MOD;

            exp >>= 1;
        }

        res as i32
    }

    pub fn assign_edge_weights(edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let size = edges.len() + 2;
        let mut bt = BinaryLiftTree::new(size);
        let mut res = vec![0; queries.len()];

        for e in &edges {
            let (u, v) = (e[0] as usize, e[1] as usize);

            bt.add_edge(u, v);
        }

        bt.preprocess(1);

        for (i, q) in queries.iter().enumerate() {
            let (u, v) = (q[0] as usize, q[1] as usize);
            let dist = bt.get_distance(u, v) - 1;
            res[i] = Solution::bin_mod_exp(dist);
        }

        res
    }
}
