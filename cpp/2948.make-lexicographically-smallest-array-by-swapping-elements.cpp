#include <algorithm>
#include <ranges>
#include <utility>
#include <vector>

using std::vector, std::pair;

class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        const int n = nums.size();
        // sorted vector of pairs {(position, value), ...}
        auto data = nums | std::views::enumerate |
                    std::ranges::to<vector<pair<int, int>>>();

        std::ranges::sort(data, {}, &pair<int, int>::second);

        vector<int> indices({data[0].first}),
            values({data[0].second}); // buffers

        vector<int> res(n, -1);

        auto drain = [](vector<int>& res, vector<int>& indices,
                        vector<int>& values) -> void {
            std::ranges::sort(indices);

            for (auto [k, j] : std::views::enumerate(indices)) {
                res[j] = values[k];
            }

            values.clear();
            indices.clear();
        };

        for (int i = 1; i < n; i++) {
            if (data[i].second - data[i - 1].second > limit) {
                drain(res, indices, values);
            }

            indices.push_back(data[i].first);
            values.push_back(data[i].second);
        }

        drain(res, indices, values);

        return res;
    }
};