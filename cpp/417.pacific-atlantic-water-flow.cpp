#include <deque>
#include <utility>
#include <vector>

using std::vector, std::deque, std::pair;

typedef pair<int, int> Pair;
typedef deque<Pair> Queue;
typedef vector<vector<int>> Matrix;
typedef vector<vector<bool>> Visited;

const int DIR[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

class Island {
public:
  Island(const Matrix &heights)
      : ROWS(heights.size()), COLS(heights.front().size()), heights(heights),
        vis(ROWS, vector<bool>(COLS, false)) {}

  void bfs(int r, int c) {
    if (vis[r][c]) {
      return;
    }

    Queue q;
    q.push_back(Pair(r, c));
    vis[r][c] = true;

    while (q.size()) {
      auto [r, c] = q.front();
      q.pop_front();

      for (auto [dr, dc] : DIR) {
        int nr = r + dr, nc = c + dc;

        if (nr < 0 || nr >= ROWS || nc < 0 || nc >= COLS) {
          continue;
        }

        if (vis[nr][nc]) {
          continue;
        }

        if (heights[r][c] > heights[nr][nc]) {
          continue;
        }

        q.push_back(Pair(nr, nc));
        vis[nr][nc] = true;
      }
    }
  }

  bool visited(int r, int c) { return vis[r][c]; }

private:
  const int ROWS;
  const int COLS;
  const Matrix &heights;

  Visited vis;
};

class Solution {
public:
  vector<vector<int>> pacificAtlantic(vector<vector<int>> &heights) {
    const int ROWS = heights.size(), COLS = heights.front().size();
    Island pacific(heights), atlantic(heights);
    Matrix both;

    for (int r = 0; r < ROWS; r++) {
      pacific.bfs(r, 0);
      atlantic.bfs(r, COLS - 1);
    }

    for (int c = 0; c < COLS; c++) {
      pacific.bfs(0, c);
      atlantic.bfs(ROWS - 1, c);
    }

    for (int r = 0; r < ROWS; r++) {
      for (int c = 0; c < COLS; c++) {
        if (pacific.visited(r, c) && atlantic.visited(r, c)) {
          both.push_back({r, c});
        }
      }
    }

    return both;
  }
};