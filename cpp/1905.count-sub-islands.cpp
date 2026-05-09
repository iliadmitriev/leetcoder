#include <queue>
#include <utility>
#include <vector>

using std::vector;

class Solution {
private:
  typedef vector<vector<int>> Matrix;
  typedef vector<vector<bool>> MatrixVisited;
  typedef std::pair<int, int> Point;

  int bfsCountSubIsland(int row, int col, const Matrix &grid1,
                        const Matrix &grid2, MatrixVisited &visited) {

    int M = grid1.size(), N = grid1.front().size();
    if (row < 0 || row >= M || col < 0 || col >= N || visited[row][col] ||
        grid2[row][col] == 0) {
      return 1;
    }

    visited[row][col] = true;

    int isSubIsland = grid1[row][col];

    isSubIsland *= bfsCountSubIsland(row + 1, col, grid1, grid2, visited);
    isSubIsland *= bfsCountSubIsland(row, col + 1, grid1, grid2, visited);
    isSubIsland *= bfsCountSubIsland(row - 1, col, grid1, grid2, visited);
    isSubIsland *= bfsCountSubIsland(row, col - 1, grid1, grid2, visited);

    return isSubIsland;
  }

public:
  int countSubIslands(vector<vector<int>> &grid1, vector<vector<int>> &grid2) {
    int M = grid1.size(), N = grid1.front().size();

    MatrixVisited visited(M, vector<bool>(N, false));

    int count = 0;

    for (int r = 0; r < M; ++r) {
      for (int c = 0; c < N; ++c) {
        if (!visited[r][c] && grid2[r][c] == 1) {
          count += bfsCountSubIsland(r, c, grid1, grid2, visited);
        }
      }
    }

    return count;
  }
};