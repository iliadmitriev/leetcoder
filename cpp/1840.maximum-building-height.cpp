#include <algorithm>
#include <utility>
#include <vector>

using std::vector, std::pair;

class Solution {
private:
    /*
    slope eq: dy = m * dx
    left A (m = 1, leaned right): y1 - y = x1 - x
    right B (m = -1, leaned left): y2 - y = -1 * (x1 - x)
    A + B:
    y1 + y2 - y - y = x1 - x - x1 + x
    y = (y1 + y2 - x1 + x2) / 2

    max height is a:
    y coordinate of intersection of two slopes the left (leaned right)
    and the right (leaned left)
    */
    inline int solve(pair<int, int>& p1, pair<int, int>& p2) {
        return (p1.second + p2.second - p1.first + p2.first) / 2;
    };

    /*
    limit between two heights
    height is limited by the distance
    dy <= dx
    abs(y2 - y1) <= abs(x2 - x1) drop left abs
    y2 <= y1 + abs(x2 - x1)
    */
    inline int cap(pair<int, int>& p1, pair<int, int>& p2) {
        return std::min(p2.second, p1.second + std::abs(p2.first - p1.first));
    };

public:
    int maxBuilding(int n, vector<vector<int>>& restrictions) {
        int topHeight = 0;
        vector<pair<int, int>> R;
        R.reserve(restrictions.size() + 2);

        R.emplace_back(1, 0); // start
        for (const auto& r : restrictions) {
            R.emplace_back(r[0], r[1]);
        }

        std::ranges::sort(R);

        // if last building is not restricted
        // add a restriction, a maximum possible value (n - 1)
        if (R.back().first < n) {
            R.emplace_back(n, n - 1);
        }

        int k = R.size();

        // cap height: left to right
        for (int i = 1; i < k; i++) {
            R[i].second = cap(R[i - 1], R[i]);
        }

        // cap height: right to left
        for (int i = k - 2; i >= 0; i--) {
            R[i].second = cap(R[i + 1], R[i]);
        }

        // get max height two slope method
        for (int i = 1; i < k; i++) {
            int y = solve(R[i - 1], R[i]);
            topHeight = std::max(topHeight, y);
        }

        return topHeight;
    }
};