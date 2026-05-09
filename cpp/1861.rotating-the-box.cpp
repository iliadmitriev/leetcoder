#include <vector>
using std::vector;

class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        const int m = boxGrid.size();
        const int n = boxGrid.front().size();
        const char empty = '.', stone = '#', obst = '*';

        vector<vector<char>> box(n, vector<char>(m, empty));

        for (int i = 0; i < m; i++) {
            for (int k = n - 1, j = n - 1; j >= 0; j--) {
                if (boxGrid[i][j] == obst) {
                    k = j;
                    box[k--][m - i - 1] = obst;
                } else if (boxGrid[i][j] == stone) {
                    box[k--][m - i - 1] = stone;
                }
            }
        }

        return box;
    }
};