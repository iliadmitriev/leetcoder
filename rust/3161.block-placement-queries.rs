use std::cmp;
use std::collections::BTreeSet;

struct SegmentTree {
    tree: Vec<i32>,
    n: usize,
}

impl SegmentTree {
    fn new(max_idx: usize) -> Self {
        let mut n = 1;

        while n <= max_idx {
            n <<= 1;
        }

        Self {
            tree: vec![0; 2 * n],
            n,
        }
    }

    // updates the value at idx to val and propagates the change upward
    // `idx` 0-based index in the logical array
    // `val` new value to store
    // time complexity: O(log N)
    fn update(&mut self, idx: usize, val: i32) {
        let mut pos = idx + self.n; // shift index to leaves
        self.tree[pos] = val;

        pos >>= 1;
        while pos > 0 {
            self.tree[pos] = cmp::max(
              self.tree[2 * pos],
              self.tree[2 * pos + 1],
            );

            pos >>= 1;
        }
    }

    // queries the maximum values in the inclusive range [l, r]
    // `l`, `r` 0-based range boundaries
    // time complexity: O(log N)
    fn query(&self, l: usize, r: usize) -> i32 {
        if l > r {
            return 0;
        }

        let (mut l, mut r) = (l + self.n, r + self.n); // shift to leaves indices
        let mut max_gap = 0;

        while l <= r {
            if l & 1 == 1{
                max_gap = max_gap.max(self.tree[l]);
                l += 1;
            }

            if r & 1 == 0 {
                max_gap = max_gap.max(self.tree[r]);
                r -= 1;
            }

            l >>= 1;
            r >>= 1;
        }

        max_gap
    }
}

struct FenwickTree {
  tree: Vec<i32>,
  n: usize,
}

impl FenwickTree {
  fn with_capacity(n: usize) -> Self {
    Self{
      tree: vec![0; n],
      n: n,
    }
  }

  fn update(&mut self, x: i32, v: i32) {
    let mut x = x as usize;
    while x < self.n {
      self.tree[x] = self.tree[x].max(v);
      x += x & (!x + 1); // down
    }
  }

  fn query(&self, x: i32) -> i32 {
    let mut x = x as usize;
    let mut res = 0;

    while x > 0 {
      res = res.max(self.tree[x]);
      x -= x & (!x + 1);
    }

    res
  }
}

impl Solution {
    pub fn get_results(queries: Vec<Vec<i32>>) -> Vec<bool> {
      let mx = queries.iter().map(|q| q[1]).max().unwrap_or(0);
      let mut st = BTreeSet::new();


      // init B-tree: [0, mx + 1] with obstacles
      let right_boundary = mx + 1;
      st.insert(0);
      st.insert(right_boundary);
      for q in &queries {
        if q[0] == 1 {
          st.insert(q[1]); // insert all obstacles
        }
      }

      let mut results = Vec::with_capacity(queries.len());

      // init fenwick tree with segments beetween obstacles
      let mut bt = FenwickTree::with_capacity((mx + 1) as usize);
      
      let mut pre = 0;
      for &x in st.iter() {
        if x == 0 {
          continue;
        }

        bt.update(x, x - pre);
        pre = x;
      }


      for q in queries.iter().rev() {
        match &q[..] {
          // type 1: add obstacle x
          [1, x] => {
            let pre_val = st.range(..x).next_back().copied().unwrap_or(0);
            let next = st.range((x + 1)..).next().copied().unwrap_or(mx);

            bt.update(next, next - pre_val);
            st.remove(&x);
          },
          // type 2: check if block of size sz fits to [0, x]
          [2, x, sz] => {
            let pre_val = st.range(..x).next_back().copied().unwrap_or(0);
            let max_space = bt.query(pre_val).max(x - pre_val);

            results.push(max_space >= *sz);
          },
          _ => unreachable!(),
        }
      }

      results.reverse();
      results
    }
}
