impl Solution {
    pub fn minimum_cost(mut cost: Vec<i32>) -> i32 {
        cost.sort_unstable_by(|a, b| b.cmp(a));
        
        cost
          .chunks(3)
          .flat_map(|chunk| chunk.iter().copied().take(2))
          .sum()  
    }
}
