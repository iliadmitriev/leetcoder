impl Solution {
    pub fn mirror_distance(n: i32) -> i32 {
        return (n - Self::reverse(n)).abs();
    }

    fn reverse(x: i32) -> i32 {
        let mut res = 0;
        let mut x = x;

        while x > 0 {
            res = res * 10 + x % 10;
            x /= 10;
        }

        res
    }
}