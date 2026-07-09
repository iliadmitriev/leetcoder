struct UF {
    par: Vec<usize>,
    sz: usize,
}

impl UF {
    pub fn new(sz: usize) -> Self {
        Self {
            par: (0..sz).collect(),
            sz: sz,
        }
    }

    pub fn find(&mut self, mut x: usize) -> usize {
        while (x != self.par[x]) {
            let par = self.par[x];
            self.par[x] = self.par[par];
            x = self.par[x];
        }

        x
    }

    pub fn join(&mut self, x: usize, y: usize) -> bool {
        let par_x = self.find(x);
        let par_y = self.find(y);

        if par_x == par_y {
            return false;
        }

        self.par[par_y] = par_x;
        true
    }

    pub fn joined(&mut self, x: usize, y: usize) -> bool {
        let par_x = self.find(x);
        let par_y = self.find(y);

        par_x == par_y
    }
}

impl Solution {
    pub fn path_existence_queries(
        n: i32,
        nums: Vec<i32>,
        max_diff: i32,
        queries: Vec<Vec<i32>>,
    ) -> Vec<bool> {
        let m = queries.len();
        let mut res = vec![false; m];
        let mut uf = UF::new(n as usize);

        for i in (1..n as usize) {
            if (nums[i] - nums[i - 1] <= max_diff) {
                uf.join(i - 1, i);
            }
        }

        for (j, q) in queries.iter().enumerate() {
            res[j] = uf.joined(q[0] as usize, q[1] as usize);
        }

        res
    }
}
