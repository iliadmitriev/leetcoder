impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        std::iter::once(0)
          .chain(gain
            .into_iter()
            .scan(0, |cur_total, cur_gain| {
              *cur_total += cur_gain;
              Some(*cur_total)
            })
          )
          .max()
          .unwrap_or(0)

        // gain.into_iter()
        //     .fold((0, 0), |(running_total, running_max), current| {
        //         let next_total = running_total + current;
        //         (next_total, running_max.max(next_total))
        //     })
        //     .1 // take second value
    }
}
