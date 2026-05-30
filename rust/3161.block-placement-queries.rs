use std::cmp;

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

impl Solution {
    pub fn get_results(queries: Vec<Vec<i32>>) -> Vec<bool> {
      let max_x = queries.iter().map(|q| q[1] as usize).max().unwrap_or(0);
      let mut seg = SegmentTree::new(max_x + 2);

      // init tree: [0, max_x + 1]
      let right_boundary = max_x + 1;
      let mut obs = vec![0, right_boundary as i32];
      seg.update(right_boundary, right_boundary as i32);

      let mut results = Vec::with_capacity(queries.len());

      for q in &queries {
        match &q[..] {
          // type 1: add obstacle x
          [1, x] => {
            // idx - insertion point
            let idx = match obs.binary_search(x) {
              Err(i) => i,
              Ok(_) => unreachable!("duplicate item"),
            };

            let prev = obs[idx - 1];
            let next = obs[idx];

            seg.update(*x as usize, *x - prev);
            seg.update(next as usize, next - *x);

            obs.insert(idx, *x); // optimized memmove
          },
          // type 2: check if block of size sz fits to [0, x]
          [2, x, sz] => {
            let x_val = *x as usize;

            let idx = match obs.binary_search(x) {
              Ok(i) => i,
              Err(i) => i - 1,
            };

            let last_obs = obs[idx];

            let max_gap = seg.query(0, x_val).max(x_val as i32 - last_obs);

            results.push(max_gap >= *sz);
          },
          _ => unreachable!(),
        }
      }

      results
    }
}
