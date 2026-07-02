use std::collections::BinaryHeap;

impl Solution {
    pub fn find_safe_walk(grid: Vec<Vec<i32>>, health: i32) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        
        let sides = [(0i32, 1i32), (1, 0), (0, -1), (-1, 0)];
        let finish_r = m - 1;
        let finish_c = n - 1;
        
        let mut health = health - grid[0][0];
        
        // BinaryHeap in Rust is a max-heap by default.
        // It stores (health, r, c) and naturally orders by health descending.
        let mut pq = BinaryHeap::new();
        pq.push((health, 0usize, 0usize));
        
        let mut vis = vec![vec![false; n]; m];
        vis[0][0] = true;
        
        while let Some((h, r, c)) = pq.pop() {
            if r == finish_r && c == finish_c {
                return true;
            }
            
            for &(dr, dc) in &sides {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                
                if nr < 0 || nr >= m as i32 || nc < 0 || nc >= n as i32 {
                    continue;
                }
                
                let nr = nr as usize;
                let nc = nc as usize;
                
                let new_health = h - grid[nr][nc];
                if new_health <= 0 || vis[nr][nc] {
                    continue;
                }
                
                vis[nr][nc] = true;
                pq.push((new_health, nr, nc));
            }
        }
        
        false
    }
}