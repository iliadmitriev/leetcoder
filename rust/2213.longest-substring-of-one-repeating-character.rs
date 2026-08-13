use std::cmp; // min, max

struct SegmentTree {
    n: usize,
    buf: Vec<char>,
    pre: Vec<i32>,
    suf: Vec<i32>,
    best: Vec<i32>,
}

impl SegmentTree {
    fn from(s: String) -> Self {
        let n = s.len();
        let buf: Vec<char> = s.chars().collect();
        let pre = vec![0; n << 2];
        let suf = vec![0; n << 2];
        let best = vec![0; n << 2];

        let mut tree = Self {
            n: n,
            buf: buf,
            pre: pre,
            suf: suf,
            best: best,
        };
        tree.build(1, 0, n - 1);

        tree
    }

    fn build(&mut self, node: usize, l: usize, r: usize) -> () {
        // base
        if l == r {
            self.pre[node] = 1;
            self.suf[node] = 1;
            self.best[node] = 1;

            return ();
        }

        let mid = (l + r) >> 1;

        self.build(node << 1, l, mid);
        self.build(node << 1 | 1, mid + 1, r);

        self.update_node(node, l, r);
    }

    fn update_node(&mut self, node: usize, l: usize, r: usize) -> () {
        // base (when parts left and right do not match)
        let left = node << 1;
        let right = node << 1 | 1;

        self.pre[node] = self.pre[left];
        self.suf[node] = self.suf[right];
        self.best[node] = cmp::max(self.best[left], self.best[right]);

        // if parts match, can be connected
        let mid = (l + r) >> 1;
        if self.buf[mid] == self.buf[mid + 1] {
            let len_left = (mid - l + 1) as i32;
            let len_right = (r - mid) as i32;

            if len_left == self.pre[left] {
                self.pre[node] = self.pre[left] + self.pre[right];
            }

            if len_right == self.suf[right] {
                self.suf[node] = self.suf[left] + self.suf[right];
            }

            self.best[node] = self.best[node].max(self.suf[left] + self.pre[right])
        }
    }

    fn update(&mut self, node: usize, l: usize, r: usize, i: usize) -> () {
        // base
        if l == r {
            return;
        }

        let mid = (l + r) >> 1;

        if i <= mid {
            self.update(node << 1, l, mid, i);
        } else {
            self.update(node << 1 | 1, mid + 1, r, i);
        }

        self.update_node(node, l, r)
    }

    fn update_char_at(&mut self, ch: char, pos: i32) -> () {
        let pos = pos as usize;

        self.buf[pos] = ch;
        self.update(1, 0, self.n - 1, pos);
    }

    fn get_best(&self) -> i32 {
        self.best[1]
    }
}

impl Solution {
    pub fn longest_repeating(
        s: String,
        query_characters: String,
        query_indices: Vec<i32>,
    ) -> Vec<i32> {
        let k = query_characters.len();
        let mut res = vec![0; k];
        let mut tree = SegmentTree::from(s);

        for (i, (ch, &idx)) in query_characters
            .chars()
            .zip(query_indices.iter())
            .enumerate()
        {
            tree.update_char_at(ch, idx);
            res[i] = tree.get_best();
        }

        res
    }
}
