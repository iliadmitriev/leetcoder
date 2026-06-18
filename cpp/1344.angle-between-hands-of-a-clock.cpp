class Solution {
public:
    double angleClock(int hour, int minutes) {
        const double minuteHour = 60.0;
        const double oneHour = 30.0;
        const double oneMinute = 6.0;
        const double half = 180.0;
        const int hours = 12;

        hour %= hours;

        double minuteDegree = minutes * oneMinute;
        double hourDegree = hour * oneHour + oneHour * (minutes / minuteHour);
        double angle =  std::abs(minuteDegree - hourDegree);

        if (angle > half) {
          angle = 2 * half - angle;
        }

        return angle;
    }
};