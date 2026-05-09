impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        // odd numbers between [0,x] inclusive is (x + 1) / 2
        // ood numbers between [0,x) exclusive is x / 2

        (high + 1) / 2 - low / 2
    }
}