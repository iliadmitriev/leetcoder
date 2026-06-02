use std::cmp;


impl Solution {
    pub fn earliest_finish_time(land_start_time: Vec<i32>, land_duration: Vec<i32>, water_start_time: Vec<i32>, water_duration: Vec<i32>) -> i32 {
        let best_water = water_start_time
          .iter()
          .zip(water_duration.iter())
          .map(|(&s, &d)| s + d)
          .min()
          .unwrap();

        let best_land = land_start_time
          .iter()
          .zip(land_duration.iter())
          .map(|(&s, &d)| s + d)
          .min()
          .unwrap();

        let best_water_land = land_start_time
          .iter()
          .zip(land_duration.iter())
          .map(|(&s, &d)| s.max(best_water) + d)
          .min()
          .unwrap();

        let best_land_water = water_start_time
          .iter()
          .zip(water_duration.iter())
          .map(|(&s, &d)| s.max(best_land) + d)
          .min()
          .unwrap();

        cmp::min(
          best_land_water,
          best_water_land,
        )
    }
}