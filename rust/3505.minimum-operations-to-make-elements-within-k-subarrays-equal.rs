use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap};
use std::marker::PhantomData;

// -- ordering markers
pub struct Min;
pub struct Max;

pub trait Cmp {
    fn cmp(a: &i32, b: &i32) -> Ordering;
}

impl Cmp for Min {
    fn cmp(a: &i32, b: &i32) -> Ordering { b.cmp(a) }
}

impl Cmp for Max {
    fn cmp(a: &i32, b: &i32) -> Ordering { a.cmp(b) }
}

struct Item<C: Cmp>(i32, PhantomData<C>);

impl<C: Cmp> PartialEq for Item<C> {
    fn eq(&self, other: &Self) -> bool { self.0 == other.0 }
}
impl<C: Cmp> Eq for Item<C> {}
impl<C: Cmp> PartialOrd for Item<C> {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> { Some(self.cmp(other)) }
}
impl<C: Cmp> Ord for Item<C> {
    fn cmp(&self, other: &Self) -> Ordering { C::cmp(&self.0, &other.0) }
}

pub struct HeapSum<C: Cmp> {
    sum: i64,
    size: i64,
    removed: HashMap<i32, i32>,
    q: BinaryHeap<Item<C>>,
}

impl<C: Cmp> HeapSum<C> {
    pub fn new() -> Self {
        Self {
            sum: 0,
            size: 0,
            removed: HashMap::new(),
            q: BinaryHeap::new(),
        }
    }

    pub fn size(&self) -> i64 { self.size }
    pub fn sum(&self) -> i64 { self.sum }

    pub fn top(&mut self) -> i32 {
        self.prune();
        self.q.peek().expect("top on empty HeapSum").0
    }

    pub fn push(&mut self, x: i32) {
        self.size += 1;
        self.sum += x as i64;
        self.q.push(Item(x, PhantomData));
    }

    pub fn pop(&mut self) -> i32 {
        self.prune();
        let Item(x, _) = self.q.pop().expect("pop on empty HeapSum");
        self.size -= 1;
        self.sum -= x as i64;

        x
    }

    pub fn remove(&mut self, x: i32) {
        *self.removed.entry(x).or_insert(0) += 1;
        self.size -= 1;
        self.sum -= x as i64;
        self.prune();
    }

    fn prune(&mut self) {
        while let Some(&Item(top, _)) = self.q.peek() {
            if !self.removed.contains_key(&top) {
                return;
            }

            let cnt = self.removed.get_mut(&top).unwrap();
            *cnt -= 1;
            if *cnt <= 0 {
                self.removed.remove(&top);
            }

            self.q.pop();
        }
    }
}

pub struct BalancedWindow {
    lower: HeapSum<Max>,
    upper: HeapSum<Min>,
}

impl BalancedWindow {
    pub fn new() -> Self {
        Self { lower: HeapSum::new(), upper: HeapSum::new() }
    }

    pub fn add(&mut self, x: i32) {
        if self.lower.size() == 0 || x <= self.lower.top() {
            self.lower.push(x);
        } else {
            self.upper.push(x);
        }

        self.rebalance();
    }

    pub fn remove(&mut self, x: i32) {
        if self.lower.size() > 0 && x <= self.lower.top() {
            self.lower.remove(x);
        } else {
            self.upper.remove(x);
        }

        self.rebalance();
    }

    pub fn get_ops(&mut self) -> i64 {
        let mid = self.lower.top();
        self.upper.sum() - self.lower.sum() + mid as i64 * (self.lower.size() - self.upper.size())
    }

    fn rebalance(&mut self) {
        if self.lower.size() > self.upper.size() + 1 {
            let v = self.lower.pop();
            self.upper.push(v);
        } else if self.lower.size() < self.upper.size() {
            let v = self.upper.pop();
            self.lower.push(v);
        }
    }
}

impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32, k: i32) -> i64 {
        let n = nums.len();
        let k = k as usize;
        let x = x as usize;

        let mut win = BalancedWindow::new();
        let mut ops = vec![0i64; n];

        for r in 0..n {
            win.add(nums[r]);

            if r + 1 < x {
                continue;
            }

            let l = r + 1 - x;

            ops[r] = win.get_ops();

            win.remove(nums[l]);
        }

        const INF: i64 = i64::MAX / 4;
        let mut dp = vec![vec![INF; k + 1]; n];

        for i in 0..n {
            dp[i][0] = 0;
        }

        for j in 1..=k {
            if j == 1 {
                if x - 1 < n {
                    dp[x - 1][j] = ops[x - 1];
                }
            } else {
                let end = j * x - 1;
                if end < n && dp[(j - 1) * x - 1][j - 1] != INF {
                    dp[end][j] = dp[(j - 1) * x - 1][j - 1] + ops[end];
                }
            }
        }

        for j in 1..=k {
            for i in (j * x)..n {
                let take = if i >= x { dp[i - x][j - 1] + ops[i] } else { INF };
                let skip = dp[i - 1][j];

                dp[i][j] = take.min(skip);
            }
        }

        dp[n - 1][k]
    }
}