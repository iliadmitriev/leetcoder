

class Solution {
public:
    static vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        const int R = grid.size(),
                  C = grid[0].size();  // number of rows and columns
        const int L = min(R, C) / 2;   // number of layers
        const int P = 2 * (R + C - 2); // perimeter (outer layer 0)

        vector<int> layer(P, 0); // buffer for perimeter values

        for (int d = 0; d < L; d++) { // d - layer number from 0 to L - 1
            const int si = d, ei = R - d - 1; // start and end of row indices
            const int sj = d, ej = C - d - 1; // start and end of column indices
            const int h = R - 2 * d, w = C - 2 * d; // height and width
            const int p = 2 * (h + w - 2); // perimeter for current layer

            int id = 0;
            // Extract the layer elements
            for (int j = 0; j < w - 1; j++)
                layer[id++] = grid[si][sj + j];
            for (int i = 0; i < h - 1; i++)
                layer[id++] = grid[si + i][ej];
            for (int j = 0; j < w - 1; j++)
                layer[id++] = grid[ei][ej - j];
            for (int i = 0; i < h - 1; i++)
                layer[id++] = grid[ei - i][sj];

            // rotate
            // put starting position
            id = k % p;

            for (int j = 0; j < w - 1; j++) {
                grid[si][sj + j] = layer[id];
                id = (id + 1) % p;
            }

            for (int i = 0; i < h - 1; i++) {
                grid[si + i][ej] = layer[id];
                id = (id + 1) % p;
            }

            for (int j = 0; j < w - 1; j++) {
                grid[ei][ej - j] = layer[id];
                id = (id + 1) % p;
            }

            for (int i = 0; i < h - 1; i++) {
                grid[ei - i][sj] = layer[id];
                id = (id + 1) % p;
            }
        }
        return grid;
    }
};
