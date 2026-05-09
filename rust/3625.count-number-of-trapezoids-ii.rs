use std::collections::HashMap;

fn gcd(mut a: i32, mut b: i32) -> i32 {
    a = a.abs();
    b = b.abs();

    while b != 0 {
        let tmp = a % b;
        a = b;
        b = tmp;
    }
    a
}

fn count_collinear<T>(mp: &HashMap<T, Vec<i32>>) -> i32 {
    let mut total: i64 = 0;
    for bs in mp.values() {
        if bs.len() < 2 {
            continue;
        }

        let uniq = bs.into_iter().fold(HashMap::new(), |mut acc, b| {
            *acc.entry(b).or_insert(0) += 1;
            acc
        });

        let mut cnt = 0;
        for k in uniq.values() {
            total += cnt * k;
            cnt += k;
        }
    }

    total as i32
}

impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        let mut slopes: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut mids: HashMap<i32, Vec<i32>> = HashMap::new(); // to count parallelograms

        for i in 0..points.len() {
            let x1 = points[i][0];
            let y1 = points[i][1];

            for j in i + 1..points.len() {
                let x2 = points[j][0];
                let y2 = points[j][1];

                let mut dx = x2 - x1;
                let mut dy = y2 - y1;

                if dx < 0 || (dx == 0 && dy < 0) {
                    dx = -dx;
                    dy = -dy;
                }

                let g = gcd(dx, dy.abs());
                let sx = dx / g;
                let sy = dy / g;

                let b = sx * y1 - sy * x1;

                let k1 = sx << 12 | (sy + 2000);
                let k2 = dx << 12 | (dy + 2000);

                slopes.entry(k1).or_default().push(b);
                mids.entry(k2).or_default().push(b);
            }
        }

        // total number of trapezoids:
        // total trapazoids - number of collinear - number of parallelograms

        count_collinear(&slopes) - count_collinear(&mids) / 2
    }
}