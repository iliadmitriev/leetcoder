#include <algorithm>
#include <ranges>
#include <tuple>
#include <vector>

class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime,
                           vector<int>& landDuration,
                           vector<int>& waterStartTime,
                           vector<int>& waterDuration) {

        auto get_min_zip_sum = [](const std::vector<int>& start,
                                  const std::vector<int>& duration, auto op) {
            return std::ranges::min(std::views::zip(start, duration) |
                                    std::views::transform(op));
        };

        int bestLand = get_min_zip_sum(
            landStartTime, landDuration, [](auto const& pair) -> int {
                return std::get<0>(pair) + std::get<1>(pair);
            });
        int bestWater = get_min_zip_sum(
            waterStartTime, waterDuration, [](auto const& pair) -> int {
                return std::get<0>(pair) + std::get<1>(pair);
            });

        // best water then land
        int bestWaterLand = get_min_zip_sum(
            landStartTime, landDuration, [bestWater](auto const& pair) -> int {
                return std::max(std::get<0>(pair), bestWater) +
                       std::get<1>(pair);
            });

        // best land then water
        int bestLandWater = get_min_zip_sum(
            waterStartTime, waterDuration, [bestLand](auto const& pair) -> int {
                return std::max(std::get<0>(pair), bestLand) +
                       std::get<1>(pair);
            });

        return std::min(bestWaterLand, bestLandWater);
    }
};