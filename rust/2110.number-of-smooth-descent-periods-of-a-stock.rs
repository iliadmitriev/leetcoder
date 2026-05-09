
impl Solution {
    pub fn get_descent_periods(prices: Vec<i32>) -> i64 {
        let mut prev = -1;
        let mut window = 1;
        let mut total: i64 = 0;

        prices.iter().for_each(|&price| {
            if prev - 1 == price {
                window += 1;
            } else {
                window = 1;
            }

            total += window as i64;
            prev = price;
        });

        total
    }
}