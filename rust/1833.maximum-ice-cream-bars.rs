use std::cmp;

impl Solution {
    pub fn max_ice_cream(costs: Vec<i32>, coins: i32) -> i32 {
        let Some(&max_cost) = costs.iter().max() else {
            return 0;
        };

        let max_cost = max_cost as usize;
        let mut counts = vec![0; max_cost + 1];
        let mut coins = coins;
        let mut bars = 0;

        for &cost in costs.iter() {
            counts[cost as usize] += 1;
        }

        for cost in 1..=max_cost {
            let cost_i32 = cost as i32;

            if coins < cost_i32 as i32 {
                break;
            }

            if counts[cost] == 0 {
                continue;
            }

            let can_buy = cmp::min(counts[cost], coins / cost_i32);
            coins -= cost_i32 * can_buy;
            bars += can_buy;
        }

        bars
    }
}
