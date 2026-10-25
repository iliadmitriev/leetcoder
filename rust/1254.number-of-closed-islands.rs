impl Solution {
    pub fn closed_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut res = 0;

        for r in (0..m) {
            for c in (0..n) {
                if grid[r][c] == 0 && Self::dfs_fill(&mut grid, r as i32, c as i32) {
                    res += 1;
                }
            }
        }

        res
    }

    fn dfs_fill(g: &mut Vec<Vec<i32>>, r: i32, c: i32) -> bool {
        let rows = g.len() as i32;
        let cols = g[0].len() as i32;

        if r < 0 || c < 0 || r >= rows || c >= cols {
            return false;
        }

        if g[r as usize][c as usize] == 1 {
            return true;
        }

        g[r as usize][c as usize] = 1;

        let up = Self::dfs_fill(g, r - 1, c);
        let down = Self::dfs_fill(g, r + 1, c);
        let left = Self::dfs_fill(g, r, c - 1);
        let right = Self::dfs_fill(g, r, c + 1);

        up && down && left && right
    }
}
