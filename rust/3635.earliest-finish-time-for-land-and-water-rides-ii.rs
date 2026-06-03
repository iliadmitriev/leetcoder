use std::cmp;

impl Solution {
    pub fn earliest_finish_time(
        land_start_time: Vec<i32>,
        land_duration: Vec<i32>,
        water_start_time: Vec<i32>,
        water_duration: Vec<i32>,
    ) -> i32 {
        let best_land = land_start_time
            .iter()
            .zip(land_duration.iter())
            .map(|(&s, &e)| s + e)
            .min()
            .unwrap_or(0);

        let best_water = water_start_time
            .iter()
            .zip(water_duration.iter())
            .map(|(&s, &e)| s + e)
            .min()
            .unwrap_or(0);

        let best_land_water = water_start_time
            .iter()
            .zip(water_duration.iter())
            .map(|(&s, &e)| best_land.max(s) + e)
            .min()
            .unwrap_or(best_land);

        let best_water_land = land_start_time
            .iter()
            .zip(land_duration.iter())
            .map(|(&s, &e)| best_water.max(s) + e)
            .min()
            .unwrap_or(best_water);

        return cmp::min(best_land_water, best_water_land);
    }
}
