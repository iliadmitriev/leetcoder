use std::collections::HashMap;

pub struct BinaryIndexTree {
    size: usize,
    tree1: Vec<i64>,
    tree2: Vec<i64>,
}

impl BinaryIndexTree {
    pub fn new(size: usize) -> Self {
        Self {
            size: size,
            tree1: vec![0; size + 1],
            tree2: vec![0; size + 1],
        }
    }

    pub fn add(&mut self, left: usize, right: usize, delta: i64) {
        self._add(left, delta); // start applying the delta
        self._add(right + 1, -delta) // cancel applying the delta
    }

    pub fn query(&self, left: usize, right: usize) -> i64 {
        self._query(right) - self._query(left - 1)
    }

    fn _lowbit(index: usize) -> usize {
        index & index.wrapping_neg()
    }

    fn _add(&mut self, mut index: usize, delta: i64) {
        let value = (index as i64) * delta; // set multiplier
        index += 1; // shift index

        while (index <= self.size) {
            self.tree1[index] += delta;
            self.tree2[index] += value;

            index += BinaryIndexTree::_lowbit(index);
        }
    }

    fn _query(&self, mut index: usize) -> i64 {
        index += 1;
        let mul = index as i64;

        let mut res = 0 as i64;

        while (index > 0) {
            res += mul * self.tree1[index] - self.tree2[index];

            index -= BinaryIndexTree::_lowbit(index);
        }

        res
    }
}

impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        let MOD = 1_000_000_007 as i64;
        let n = nums.len();

        let mut res = 0 as i64;
        let mut cur = 0 as i64;
        let mut seen: HashMap<i32, usize> = HashMap::new();
        let mut bit = BinaryIndexTree::new(n + 1);

        for (i, &x) in nums.iter().enumerate() {
            let j = match seen.get(&x) {
                Some(&v) => v + 1,
                None => 0,
            };

            let size = (i + 1 - j) as i64;

            let q = bit.query(j, i);

            cur = (cur + 2 * q + size) % MOD;
            res = (res + cur) % MOD;

            bit.add(j, i, 1);
            seen.insert(x, i);
        }

        res as i32
    }
}
