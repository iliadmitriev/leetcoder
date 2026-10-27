impl Solution {
    pub fn create_grid(m: i32, n: i32) -> Vec<String> {
        let mut grid = vec![vec!['#'; n as usize]; m as usize];
        let slope = |r: i32, c: i32| -> i32 { (m * r - c * n).abs() };

        let mut r = 0;
        let mut c = 0;
        grid[r as usize][c as usize] = '.';

        while r < m - 1 || c < n - 1 {
            if c == n - 1 || (r < m - 1 && slope(r + 1, c) < slope(r, c + 1)) {
                r += 1;
            } else {
                c += 1;
            }

            grid[r as usize][c as usize] = '.';
        }

        grid.into_iter()
            .map(|row| row.into_iter().collect::<String>())
            .collect()
    }
}
