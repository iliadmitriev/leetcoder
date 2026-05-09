impl Solution {
    pub fn number_of_ways(corridor: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        const PLANT: char = 'P';
        const SEAT: char = 'S';

        let mut div = 1;
        let mut seats = 0;
        let mut count: i64 = 1;

        for c in corridor.chars() {
            match seats {
                2 => {
                    if c == PLANT {
                        div += 1;
                    } else {
                        count = (count * div) % MOD;
                        div = 1;
                        seats = 1;
                    }
                }
                _ => {
                    if c == SEAT {
                        seats += 1;
                    }
                }
            }
        }

        if seats != 2 {
            return 0;
        }

        count as i32
    }
}