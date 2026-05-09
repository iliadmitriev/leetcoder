impl Solution {
    pub fn furthest_distance_from_origin(moves: String) -> i32 {
        let mut pos = 0i32;
        let mut spc = 0i32;

        for m in moves.chars() {
            match m {
                'L' => pos -= 1,
                'R' => pos += 1,
                '_' => spc += 1,
                _ => unreachable!("this never happen"),
            }
        }

        return pos.abs() + spc;
    }
}
