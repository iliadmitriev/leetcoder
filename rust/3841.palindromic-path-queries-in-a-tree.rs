pub struct BinaryIndexTree {
    n: usize,
    tree: Vec<i32>,
}

impl BinaryIndexTree {
    pub fn new(n: usize) -> Self {
        Self {
            n: n,
            tree: vec![0; n + 1],
        }
    }

    fn low_bit(x: usize) -> usize {
        x & x.wrapping_neg()
    }

    pub fn query(&self, mut i: usize) -> i32 {
        let mut res = 0;
        while (i > 0) {
            res ^= self.tree[i];
            i -= Self::low_bit(i);
        }

        res
    }

    pub fn update(&mut self, mut i: usize, v: i32) {
        while (i <= self.n) {
            self.tree[i] ^= v;
            i += Self::low_bit(i);
        }
    }

    pub fn update_range(&mut self, l: usize, r: usize, v: i32) {
        self.update(l, v);
        self.update(r + 1, v);
    }
}

pub struct BinaryUpliftTree {
    n: usize,
    LOG: usize,
    t: usize,
    tree: Vec<Vec<usize>>, // uplift tree
    l: Vec<usize>,         // pre-order indices of nodes
    r: Vec<usize>,         // post-order indices of nodes
    dep: Vec<i32>,         // depths of the nodes
}

impl BinaryUpliftTree {
    pub fn new(n: usize) -> Self {
        let LOG = (usize::BITS - n.leading_zeros()) as usize;

        Self {
            n: n,
            LOG: LOG,
            t: 0,
            tree: vec![vec![0; LOG]; n],
            l: vec![0; n],
            r: vec![0; n],
            dep: vec![0; n],
        }
    }

    fn dfs(&mut self, g: &[Vec<usize>], u: usize, p: usize) {
        self.t += 1;
        self.l[u] = self.t;
        self.tree[u][0] = p;

        for &v in g[u].iter() {
            if v == p {
                continue;
            }

            self.dep[v] = self.dep[u] + 1;
            self.dfs(g, v, u);
        }

        self.r[u] = self.t;
    }

    pub fn build(&mut self, g: &[Vec<usize>]) {
        self.dfs(g, 0, 0);

        for j in (1..self.LOG) {
            for i in (0..self.n) {
                let prev = self.tree[i][j - 1];
                self.tree[i][j] = self.tree[prev][j - 1];
            }
        }
    }

    pub fn lca(&self, mut u: usize, mut v: usize) -> usize {
        if self.dep[u] < self.dep[v] {
            (u, v) = (v, u);
        }

        let diff = self.dep[u] - self.dep[v];
        for j in (0..self.LOG) {
            if (diff >> j) & 1 == 1 {
                u = self.tree[u][j];
            }
        }

        if u == v {
            return u;
        }

        for j in (0..self.LOG).rev() {
            if self.tree[u][j] != self.tree[v][j] {
                u = self.tree[u][j];
                v = self.tree[v][j];
            }
        }

        return self.tree[u][0];
    }

    pub fn left(&self, i: usize) -> usize {
        self.l[i]
    }

    pub fn right(&self, i: usize) -> usize {
        self.r[i]
    }
}

impl Solution {
    pub fn palindrome_path(
        n: i32,
        edges: Vec<Vec<i32>>,
        s: String,
        queries: Vec<String>,
    ) -> Vec<bool> {
        let n = n as usize;
        let mut s: Vec<u8> = s.bytes().collect();
        let char_bit = |ch: u8| -> i32 { 1 << (ch - b'a') };

        let mut graph = vec![vec![]; n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;

            graph[u].push(v);
            graph[v].push(u);
        }

        let mut res: Vec<bool> = Vec::new();
        let mut bit = BinaryIndexTree::new(n + 1);
        let mut but = BinaryUpliftTree::new(n);

        but.build(&graph); // build flat tree from graph
        for i in (0..n) {
            bit.update_range(but.left(i), but.right(i), char_bit(s[i]));
        }

        for q in queries.iter() {
            let fields: Vec<&str> = q.split_whitespace().collect();

            if fields[0] == "update" {
                let u: usize = fields[1].parse().unwrap();
                let c = fields[2].as_bytes()[0];

                let old = char_bit(s[u]);
                let new = char_bit(c);

                bit.update_range(but.left(u), but.right(u), old ^ new);
                s[u] = c;
            } else {
                let u: usize = fields[1].parse().unwrap();
                let v: usize = fields[2].parse().unwrap();
                let w = but.lca(u, v);

                let mask = bit.query(but.left(u)) ^ bit.query(but.left(v)) ^ char_bit(s[w]);
                res.push((mask & (mask - 1)) == 0);
            }
        }

        res
    }
}
