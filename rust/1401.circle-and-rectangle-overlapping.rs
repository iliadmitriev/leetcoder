use std::cmp;

impl Solution {
    pub fn check_overlap(radius: i32, x_center: i32, y_center: i32, x1: i32, y1: i32, x2: i32, y2: i32) -> bool {
        let dist = |ax, ay, bx, by| {
          let dx = ax - bx;
          let dy = ay - by;

          return dx * dx + dy * dy;
        };

        // calculate the coordinates of the rectancle point closest to the circle center
        // 3 cases (for the single coordinate, e.g. y):
        // the rectangle is above the center: y_center < y2 && y_center > y1 => y1
        // the rectangle is between the center: y_center < y2 && y_center < y1 => y_center
        // the rectangle is below the center: y_center > y2 && y2 > y1 => y2
        let x = cmp::max(x1, cmp::min(x2, x_center));
        let y = cmp::max(y1, cmp::min(y2, y_center));

        // if point x,y is inside the cirle
        return dist(x, y, x_center, y_center) <= radius * radius;
    }
}