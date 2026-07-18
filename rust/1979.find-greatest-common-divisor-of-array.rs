impl Solution {
    pub fn find_gcd(nums: Vec<i32>) -> i32 {
        let gcd1 = |mut a: i32, mut b: i32| {
            while b > 0 {
                let r = a % b;
                a = b;
                b = r;
            }

            a
        };

        let gcd2 = |mut a: i32, mut b: i32| {
            while a != b {
                if a > b {
                    a -= b;
                } else {
                    b -= a;
                }
            }

            a
        };

        let &min_value = nums.iter().min().unwrap_or(&0);
        let &max_value = nums.iter().max().unwrap_or(&0);

        gcd1(max_value, min_value)
    }
}
