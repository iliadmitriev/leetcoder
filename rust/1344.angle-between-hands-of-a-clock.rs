impl Solution {
    pub fn angle_clock(hour: i32, minute: i32) -> f64 {
       let hour = (hour % 12) as f64; // 12 -> 0
       let minute = minute as f64;

       let circle = 360.0;
       let hours = 12.0;
       let minutes = 60.0;

       let one_hour = circle / hours; // degrees in one hour (30.0)
       let one_minute = circle / minutes; // degrees in one minute (6.0)
       let one_hour_minute = circle / hours / minutes; // degrees in one hour's minute (0.5)

       let hour_anlge = hour * one_hour + minute * one_hour_minute;
       let minute_angle = minute * one_minute;

       let angle = (hour_anlge - minute_angle).abs();

       angle.min(circle - angle)
    }
}