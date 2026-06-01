#include <algorithm>
#include <execution>
#include <numeric>
#include <vector>

class Solution {
public:
    int minimumCost(vector<int>& cost) {
        const int n = cost.size();
        std::ranges::sort(cost, std::ranges::greater{});
        int total = std::reduce(std::execution::par, cost.begin(), cost.end());

        for (int i = 2; i < n; i += 3) {
            total -= cost[i];
        }

        return total;
    }
};