class Solution {
private:
  int countTotalScore(const vector<vector<int>> &grid) {
    int score = 0;
    int ROWS = grid.size(), COLS = grid[0].size();
    for (int i = 0; i < ROWS; i++) {
      for (int j = 0; j < COLS; j++) {
        score += grid[i][j] << (COLS - j - 1);
      }
    }
    return score;
  }

  void flipRow(vector<vector<int>> &grid, int row) {
    int COLS = grid[row].size();
    for (int j = 0; j < COLS; j++) {
      grid[row][j] ^= 1;
    }
  }

  void flowCol(vector<vector<int>> &grid, int col) {
    int ROWS = grid.size();
    for (int i = 0; i < ROWS; i++) {
      grid[i][col] ^= 1;
    }
  }

public:
  int matrixScore(vector<vector<int>> &grid) {
    int ROWS = grid.size(), COLS = grid[0].size();
    for (int i = 0; i < ROWS; i++) {
      if (grid[i][0] == 0) {
        flipRow(grid, i);
      }
    }

    for (int j = 1; j < COLS; j++) {
      int onesCount = 0;
      for (int i = 0; i < ROWS; i++) {
        onesCount += grid[i][j];
      }

      if (2 * onesCount < ROWS) {
        flowCol(grid, j);
      }
    }

    return countTotalScore(grid);
  }
};