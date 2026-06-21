#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        auto max_it = std::ranges::max_element(costs);

        if (max_it == costs.end()) {
            return 0; // empty vector costs
        }

        const int max_cost = *max_it;
        std::vector<int> count(max_cost + 1, 0);
        int bars = 0;

        for (int cost : costs) {
            count[cost]++;
        }

        for (int cost = 1; cost <= max_cost; cost++) {
            if (!count[cost]) {
                continue;
            }

            int can_buy = min(coins / cost, count[cost]);

            bars += can_buy;
            coins -= can_buy * cost;

            if (coins < cost) {
                break; // early return: no money to buy even a single one
            }
        }

        return bars;
    }
};