impl Solution {
    /*
    solve eq: dy = m * dx
    left A: y1 - y = 1 * (x1 - x)
    right B: y2 - y = -1 * (x2 - x)
    A+B:
    y1 - y + y2 - y = x1 - x - x2 + x
    y = (y1 + y2 - x1 + x2) / 2
    */
    fn solve(x1: i32, y1: i32, x2: i32, y2: i32) -> i32 {
      (y1 + y2 - x1 + x2) / 2
    }

    /*
    limit height of adjacent restrictions
    dy <= dx
    abs(y2 - y1) <= abs(x2 - x1), drop left abs
    y2 <= y1 + abs(x2 - x1)
    */
    fn cap(x1: i32, y1: i32, x2: i32, y2: i32) -> i32 {
      y2.min(y1 + (x2 - x1).abs())
    }

    pub fn max_building(n: i32, mut restrictions: Vec<Vec<i32>>) -> i32 {
        let mut max_height = 0;

        restrictions.insert(0, vec![1,0]);

        if let Some(last) = restrictions.last() && last[0] < n {
          restrictions.push(vec![n, n - 1]);
        }

        restrictions.sort_by_key(|x| x[0]);

        // update max height (y) left to right
        for i in 1..restrictions.len() {
          restrictions[i][1] = Solution::cap(
            restrictions[i - 1][0],
            restrictions[i - 1][1],
            restrictions[i][0],
            restrictions[i][1],
          );
        }

        for i in (0..restrictions.len()-1).rev() {
          restrictions[i][1] = Solution::cap(
            restrictions[i + 1][0],
            restrictions[i + 1][1],
            restrictions[i][0],
            restrictions[i][1],
          )
        }

        for i in 1..restrictions.len() {
          max_height = max_height.max(
            Solution::solve(
              restrictions[i - 1][0],
              restrictions[i - 1][1],
              restrictions[i][0],
              restrictions[i][1],
            ),
          );
        }

        max_height
    }
}