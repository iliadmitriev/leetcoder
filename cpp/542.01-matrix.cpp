class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        if (mat.size() == 0 || mat[0].size() == 0)
            return mat;

        int m = mat.size(), n = mat[0].size();
        int MAX = m * n;

        std::queue<int> queue;

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (mat[i][j] == 0)
                    { queue.push(i); queue.push(j); }
                else
                    mat[i][j] = MAX;

        int phase[] = {-1, 0, 1, 0, -1};
        while (!queue.empty()) {
            auto row = queue.front(); queue.pop();
            auto col = queue.front(); queue.pop();

            for (int i = 0; i < 4; i++) {
                int r = row + phase[i], c = col + phase[i + 1];
                if (r >=0 && r < m && c >= 0 && c < n && mat[r][c] > mat[row][col] + 1) {
                    queue.push(r); queue.push(c);
                    mat[r][c] = mat[row][col] + 1;
                }
            }
        }
        
        return mat;
    }
};