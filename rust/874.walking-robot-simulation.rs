use std::collections::HashSet;

impl Solution {
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
       let mut x = 0i32;
       let mut y = 0i32;
       let mut farest = 0i32;
       let mut dx = 0i32;
       let mut dy = 1i32; // face north so one step is to go up the coordinate plane

       // convert to set of obstactles
       let obst: HashSet<(i32, i32)> = obstacles
        .into_iter()
        .map(|v| (v[0], v[1]))
        .collect();

        for cmd in commands {
          match (cmd) {
            -1 => (dx, dy) = (dy, -dx), // clockwise
            -2 => (dx, dy) = (-dy, dx), // counterclockwise
            _ => {
              for _ in (0..cmd) {
                let nx = x + dx;
                let ny = y + dy;

                if obst.contains(&(nx, ny)) {
                  break;
                }

                (x, y) = (nx, ny);
              }
            },
          };

          farest = farest.max(x * x + y * y);
        }

        farest
    }
}