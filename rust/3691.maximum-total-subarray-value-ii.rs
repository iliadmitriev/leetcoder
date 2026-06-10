use std::collections::BinaryHeap;

#[derive(Clone)]
struct SegmentTree<T, F> {
    size: usize,
    identity: T,
    tree: Vec<T>,
    op: F,
}

impl<T, F> SegmentTree<T, F>
where
    T: Clone + std::marker::Copy,
    F: Fn(T, T) -> T,
{
    pub fn new(arr: &[T], identity: T, op: F) -> Self {
        let size = arr.len();
        let mut tree = vec![identity; 2 * size];

        tree[size..].copy_from_slice(arr);

        for i in (1..size).rev() {
            let left = tree[i << 1].clone();
            let right = tree[i << 1 | 1].clone();

            tree[i] = op(left, right);
        }

        Self {
            size,
            identity,
            tree,
            op,
        }
    }

    pub fn update(&mut self, idx: usize, val: T) {
        let mut idx = idx + self.size;
        self.tree[idx] = val;

        while idx > 1 {
            idx >>= 1;

            let left = self.tree[idx << 1].clone();
            let right = self.tree[idx << 1 | 1].clone();
            self.tree[idx] = (self.op)(left, right);
        }
    }

    pub fn query(&self, left: usize, right: usize) -> T {
        let mut l = left + self.size; // shift left index to leaves
        let mut r = right + self.size; // shift right index to leaves
        let mut res_r = self.identity.clone();
        let mut res_l = self.identity.clone();

        while l < r {
            if l & 1 == 1 {
                // Note: order matters for non-commutative operations: concat, ...
                res_l = (self.op)(res_l, self.tree[l].clone());
                l += 1;
            }

            if r & 1 == 1 {
                r -= 1;
                // Note: order matters for non-commutative operations: concat, ...
                res_r = (self.op)(self.tree[r].clone(), res_r);
            }

            r >>= 1;
            l >>= 1;
        }

        (self.op)(res_l, res_r)
    }
}

impl Solution {
    pub fn max_total_value(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();

        let mut st_min = SegmentTree::new(&nums, i32::MAX, |a, b| a.min(b));
        let mut st_max = SegmentTree::new(&nums, i32::MIN, |a, b| a.max(b));

        let mut q: BinaryHeap<(i32, _, _)> = (0..n)
            .map(|i| (st_max.query(i, n) - st_min.query(i, n), i, n))
            .take_while(|&x| x.0 > 0) // optimization
            .collect();

        let mut res: i64 = 0;

        for _ in 0..k {
            let (val, l, r) = q.pop().unwrap_or_default();
            res += val as i64;

            if val == 0 {
              break;
            }

            if l < r - 1 {
                let new_val = st_max.query(l, r - 1) - st_min.query(l, r - 1);
                q.push((new_val, l, r - 1));
            }
        }

        res
    }
}
