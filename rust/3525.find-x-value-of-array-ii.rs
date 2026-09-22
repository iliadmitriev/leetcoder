const MAXK: usize = 6;

struct SegmentTree {
  n: usize,
  k: usize,
  tree: Vec<Vec<usize>>,
}

impl SegmentTree {
  pub fn new(arr: Vec<i32>, k: usize) -> Self {
    let n = arr.len();
    
    let size = 2 << (n.ilog2() + (n & (n - 1) != 0) as u32);
    let tree = vec![vec![0; MAXK]; size];

    let mut t = Self{
      n: n,
      k: k,
      tree: tree,
    };

    t.build(&arr, 1, 0, n - 1);

    t
  }

  fn build(&mut self, arr: &[i32], o: usize, l: usize, r: usize) -> () {
    if l == r {
      self.make_node(o, arr[l] as usize);
      return;
    }

    let m = (l + r) / 2;
    self.build(arr, o * 2, l, m);
    self.build(arr, o * 2 + 1, m + 1, r);

    self.merge_node(o * 2, o * 2 + 1, o);
  }

  fn make_node(&mut self, o: usize, value: usize) -> () {
    self.tree[o].fill(0);
    let k = self.k;
    let r = value % k;
    self.tree[o][r] = 1; // base count
    self.tree[o][k] = r;
  }

  fn merge_node(&mut self, left: usize, right: usize, parent: usize) -> () {
    self.tree[parent].fill(0);

    let k = self.k;

    let mul_l = self.tree[left][k];
    let mul_r = self.tree[right][k];
    self.tree[parent][k] = (mul_l * mul_r) % k;

    for x in (0..k) {
      self.tree[parent][x] = self.tree[left][x];
    }

    for x in (0..k) {
      let idx = (mul_l * x) % k;
      self.tree[parent][idx] += self.tree[right][x];
    }
  }

  fn deep_merge(k: usize, a: &[usize], b: &[usize], c: &mut [usize]) {
    let mul_l = a[k];
    let mul_r = b[k];
    c[k] = (mul_l * mul_r) % k;

    for x in (0..k) {
      c[x] = a[x];
    }

    for x in (0..k) {
      let idx = (mul_l * x) % k;
      c[idx] += b[x];
    }
  }

  fn update_node(&mut self, o: usize, l: usize, r: usize, index: usize, value: usize) -> () {
    if l == r {
      self.make_node(o, value);
      return;
    }

    let m = (l + r) / 2;
    
    if index <= m {
      self.update_node(o * 2, l, m, index, value);
    } else {
      self.update_node(o * 2 + 1, m + 1, r, index, value);
    }

    self.merge_node(o * 2, o * 2 + 1, o);
  }

  fn query_node(&self, o: usize, l: usize, r: usize, L: usize, R: usize) -> Vec<usize> {
    if L <= l && r <= R {
      return self.tree[o].clone();
    }

    let m = (l + r) / 2;

    if R <= m {
      return self.query_node(o * 2, l, m, L, R);
    }

    if L > m {
      return self.query_node(o * 2 + 1, m + 1, r, L, R);
    }

    let left = self.query_node(o * 2, l, m, L, R);
    let right = self.query_node(o * 2 + 1, m + 1, r, L, R);
    let mut res = vec![0; MAXK];
    Self::deep_merge(self.k, &left, &right, &mut res);

    res
  }

  pub fn update(&mut self, index: usize, value: usize) -> () {
    self.update_node(1, 0, self.n - 1, index, value)
  }

  pub fn query(&self, L: usize, R: usize) -> Vec<usize> {
    self.query_node(1, 0, self.n - 1, L, R)
  }
}

impl Solution {
    pub fn result_array(nums: Vec<i32>, k: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let m = queries.len();
        let mut seg = SegmentTree::new(nums, k as usize);
        let mut res = vec![0; m];

        for (i, q) in queries.iter().enumerate() {
          let index = q[0] as usize;
          let value = q[1] as usize;
          let start = q[2] as usize;
          let x = q[3] as usize;

          seg.update(index, value);
          let out = seg.query(start, n - 1);

          res[i] = out[x] as i32;
        }

        res
    }
}