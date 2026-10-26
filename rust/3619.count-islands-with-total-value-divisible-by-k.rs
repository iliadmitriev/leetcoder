impl Solution {

    fn dfs(grid: &mut Vec<Vec<i32>>, r: usize, c: usize) -> i64 {
        let mut res = grid[r][c] as i64;
        grid[r][c] = 0;

        if r + 1 < grid.len() && grid[r + 1][c] != 0 {
            res += Self::dfs(grid, r + 1, c);
        }

        if r >= 1 && grid[r - 1][c] != 0 {
            res += Self::dfs(grid, r - 1, c);
        } 

        if c + 1 < grid[0].len() && grid[r][c + 1] != 0 {
            res += Self::dfs(grid, r, c + 1);
        }

        if c >= 1 && grid[r][c - 1] != 0 {
            res += Self::dfs(grid, r, c - 1);
        }

        res
    }

    pub fn count_islands(mut grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let k = k as i64;
        
        let mut count = 0;
        
        for r in (0..m) {
            for c in (0..n) {
                if grid[r][c] == 0 {
                    continue;
                }

                if Self::dfs(&mut grid, r, c) % k == 0 {
                    count += 1;
                }
            }
        }

        count
    }
}