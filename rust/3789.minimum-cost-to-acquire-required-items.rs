impl Solution {
    pub fn minimum_cost(
        cost1: i32,
        cost2: i32,
        cost_both: i32,
        need1: i32,
        need2: i32,
    ) -> i64 {
        // Приводим все переменные к i64 перед расчетами
        let cost1 = cost1 as i64;
        let cost2 = cost2 as i64;
        let cost_both = cost_both as i64;
        let mut need1 = need1 as i64;
        let mut need2 = need2 as i64;

        let mut total_cost: i64 = 0;

        if cost1 + cost2 <= cost_both {
            total_cost = need1 * cost1 + need2 * cost2;
        } else {
            let need_both = need1.min(need2);
            total_cost += need_both * cost_both;
            
            need1 -= need_both;
            need2 -= need_both;
            
            total_cost += need1 * cost1.min(cost_both);
            total_cost += need2 * cost2.min(cost_both);
        }

        total_cost
    }
}

