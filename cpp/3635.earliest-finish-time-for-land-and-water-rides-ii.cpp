#include <ranges>
#include <tuple>
#include <vector>

class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime,
                           vector<int>& landDuration,
                           vector<int>& waterStartTime,
                           vector<int>& waterDuration) {
        auto zip_map_min = [](const vector<int>& v1, const vector<int>& v2,
                              auto op) -> int {
            return std::ranges::min(std::views::zip(v1, v2) |
                                    std::views::transform(op));
        };

        int bestLand =
            zip_map_min(landStartTime, landDuration, [](const auto& p) {
                return std::get<0>(p) + std::get<1>(p);
            });

        int bestWater =
            zip_map_min(waterStartTime, waterDuration, [](const auto& p) {
                return std::get<0>(p) + std::get<1>(p);
            });

        int bestLandWater = zip_map_min(
            waterStartTime, waterDuration, [bestLand](const auto& p) {
                return std::max(bestLand, std::get<0>(p)) + std::get<1>(p);
            });

        int bestWaterLand = zip_map_min(
            landStartTime, landDuration, [bestWater](const auto& p) {
                return std::max(bestWater, std::get<0>(p)) + std::get<1>(p);
            });

        return std::min(bestLandWater, bestWaterLand);
    }
};