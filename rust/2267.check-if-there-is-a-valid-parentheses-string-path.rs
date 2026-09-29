impl Solution {
    pub fn has_valid_path(grid: Vec<Vec<char>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        let path_size = (m + n - 1) as i32;

        // heuristics:
        // 1. path size must be even to close each opening parentheses
        // 2. must not start from closing parentheses )
        // 3. must not end with opening parentheses (
        if path_size % 2 == 1 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(' {
          return false;
        }

        // memo: [m][n][path_size] = Option(bool)
        let mut memo = vec![vec![vec![None; m + n]; n]; m];

        fn dfs(
          i: usize, // row
          j: usize, // col
          mut cnt: i32, // number of parentheses (balanced at 0)
          memo: &mut Vec<Vec<Vec<Option<bool>>>>, // dynamic memo table
          m: usize, 
          n: usize,
          path_size: i32,
          grid: &Vec<Vec<char>>,
        ) -> bool {
          if i == m || j == n {
            return false;
          }

          cnt += match grid[i][j] {
            '(' => 1,
            ')' => -1,
            _ => { unreachable!(); },
          };

          // if too much closing parentheses
          // or too much opening parentheses
          if cnt < 0 || cnt > path_size / 2 {
            return false;
          }

          // base target completed
          if i == m - 1 && j == n - 1 {
            return cnt == 0;
          }

          let k = cnt as usize; // here cnt can be only greater or equal to 0

          if let Some(prev) = memo[i][j][k] {
            return prev;
          }

          let res = dfs(i + 1, j, cnt, memo, m, n, path_size, grid) || dfs(i, j + 1, cnt, memo, m, n, path_size, grid);
          memo[i][j][k] = Some(res);
          res
        };


        dfs(0, 0, 0, &mut memo, m, n, path_size, &grid)
    }
}