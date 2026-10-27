#include <string>
#include <vector>

using std::vector, std::string;

class Solution {
public:
    vector<string> createGrid(int m, int n) {
        auto slope = [&m, &n](int r, int c) -> int {
            return std::abs(m * r - n * c);
        };

        int r = 0, c = 0;
        vector<string> grid(m, string(n, '#'));
        grid[r][c] = '.';

        while (r < m - 1 || c < n - 1) {

            if ((c == n - 1) ||
                (r < m - 1 && slope(r + 1, c) < slope(r, c + 1))) {
                r++;
            } else {
                c++;
            }

            grid[r][c] = '.';
        }

        return grid;
    }
};