#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        std::ranges::sort(
            intervals, [](const vector<int>& a, const vector<int>& b) -> bool {
                if (a[0] == b[0]) {
                    return a[1] > b[1];
                }

                return a[0] < b[0];
            });

        int prev_end = 0;
        int count = 0;

        for (vector<int>& in : intervals) {
            if (in[1] > prev_end) {
                prev_end = in[1];
                count++;
            }
        }

        return count;
    }
};