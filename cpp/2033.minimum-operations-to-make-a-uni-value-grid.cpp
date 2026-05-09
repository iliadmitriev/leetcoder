#include <algorithm>
#include <vector>

using std::vector;

class Solution {

public:
    int minOperations(vector<vector<int>>& grid, int x) {
        const int remainder = grid.front().front() % x;
        const int m = grid.size(), n = grid.front().size();
        int mid, ans = 0;
        vector<int> buf;
        buf.reserve(m * n);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] % x != remainder) {
                    return -1;
                }

                buf.push_back(grid[i][j] / x);
            }
        }

        // std::sort(buf.begin(), buf.end());
        // mid = buf[m * n / 2];
        std::nth_element(buf.begin(), buf.begin() + m * n / 2, buf.end());
        mid = buf[m * n / 2];

        for (int op : buf) {
            ans += std::abs(op - mid);
        }

        return ans;
    }
};