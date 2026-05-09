impl Solution {
    pub fn count_permutations(complexity: Vec<i32>) -> i32 {
        let n = complexity.len();
        let &lowest = complexity.first().unwrap();

        for i in 1..n {
            if complexity[i] <= lowest {
                return 0;
            }
        }

        let MOD = 1_000_000_007;

        (2..n).fold(1 as i64, |acc, x| acc * (x as i64) % MOD) as i32
    }
}