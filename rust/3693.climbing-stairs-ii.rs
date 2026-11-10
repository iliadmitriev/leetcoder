impl Solution {
    pub fn climb_stairs(n: i32, costs: Vec<i32>) -> i32 {
        let mut f = 0;
        let mut f1 = 0;
        let mut f2 = 0;
        let mut f3 = 0;

        for &cost in costs.iter() {
            f = cost + (f1 + 1).min(f2 + 4).min(f3 + 9);

            f3 = f2;
            f2 = f1;
            f1 = f;
        }

        f
    }
}