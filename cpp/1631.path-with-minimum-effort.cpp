typedef array<int, 3> Effort;

class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {

        int rows = heights.size();
        int cols = heights[0].size();
        // create min priority heap queue with start position and effort of 0
        // S: O(n), n = rows * cols
        priority_queue<Effort, vector<Effort>, greater<Effort>> pq;
        pq.push({0 , 0, 0});
        // create best efforts cache with 0 effort for the start S: O(n)
        vector<vector<int>> best(rows, vector<int>(cols, numeric_limits<int>::max()));
        best[0][0] = 0;
        
        // int dirs[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
        int phases[] = {-1, 0, 1, 0, -1};

        while (!pq.empty()) {

            auto [effort, row, col] = pq.top(); pq.pop();

            // if it's a destination - return it's effort
            if (row == rows - 1 && col == cols - 1) {
                return effort;
            }
            // go in 4 directions
            for (int i = 0; i < 4; i++) {
                int nrow = row + phases[i];
                int ncol = col + phases[i + 1];

                if (0 <= nrow && nrow < rows && 0 <= ncol && ncol < cols) {
                    int neffort = max(effort, abs(heights[row][col] - heights[nrow][ncol]));
                    if (neffort < best[nrow][ncol]) {
                        best[nrow][ncol] = neffort;
                        pq.push({ neffort, nrow, ncol });
                    }
                }
            }
        }

        return 0;  
    }
};