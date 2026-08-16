impl Solution {
    pub fn stone_game_ix(stones: Vec<i32>) -> bool {
        let mut c: Vec<i32> = vec![0; 3];

        for s in stones.iter() {
            c[(s % 3) as usize] += 1;
        }

        if c[0] % 2 == 0 {
          return c[1] >= 1 && c[2] >= 1;
        }

        c[1] - c[2] > 2 || c[2] - c[1] > 2
    }
}