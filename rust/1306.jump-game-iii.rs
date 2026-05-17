use std::collections::VecDeque;

impl Solution {
    pub fn can_reach(arr: Vec<i32>, start: i32) -> bool {
        let n = arr.len();
        let mut q: VecDeque<usize> = VecDeque::with_capacity(n);
        let mut vis = vec![false; n];

        q.push_back(start as usize);

        while let Some(i) = q.pop_front() {
            if arr[i] == 0 {
                return true;
            }

            if let Some(left) = i.checked_sub(arr[i] as usize) && !vis[left] {
                vis[left] = true;
                q.push_back(left);
            }

            if let Some(right) = i.checked_add(arr[i] as usize) && right < n && !vis[right] {
                vis[right] = true;
                q.push_back(right);
            }
        }

        false
    }
}
