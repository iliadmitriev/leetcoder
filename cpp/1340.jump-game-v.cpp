#include <algorithm>
#include <ranges>
#include <vector>

class Solution {
public:
    int maxJumps(vector<int>& arr, int d) {
        const int n = arr.size();
        const int neg_inf = std::numeric_limits<int>::min();

        std::vector<int> indices(n);
        std::iota(indices.begin(), indices.end(), 0);
        std::ranges::sort(indices,
                          [&arr](int i, int j) { return arr[i] < arr[j]; });

        std::vector<int> dp(n, 0);

        for (int i : indices) {
            int max_dp = 0;
            int x = arr[i];

            // scan left: i-1 .. i-d
            {
                int max_val = neg_inf;
                auto left_indices = std::views::iota(std::max(0, i - d), i) |
                                    std::views::reverse;
                for (int j : left_indices) {

                    if (arr[j] >= x) {
                        break;
                    }

                    if (arr[j] < max_val) {
                        continue;
                    }

                    max_val = arr[j];
                    max_dp = std::max(max_dp, dp[j]);
                }
            }

            // scan right: i+1 .. i+d
            {
                int max_val = neg_inf;
                auto right_indices =
                    std::views::iota(i + 1, std::min(i + d, n - 1) + 1);
                for (int j : right_indices) {

                    if (arr[j] >= x) {
                        break;
                    }

                    if (arr[j] < max_val) {
                        continue;
                    }

                    max_val = arr[j];
                    max_dp = std::max(max_dp, dp[j]);
                }
            }

            dp[i] = 1 + max_dp;
        }

        return std::ranges::max(dp);
    }
};