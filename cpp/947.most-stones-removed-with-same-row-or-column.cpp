#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using std::unordered_map;
using std::vector;

class Solution {
private:
  typedef unordered_map<int, vector<std::pair<int, int>>> AdjList;
  typedef vector<vector<int>> EdgeList;
  typedef vector<bool> VisitedEdges;

  void dfs(AdjList &adjRow, AdjList &adjCol, VisitedEdges &visited, int edge,
           EdgeList &stones) {
    visited[edge] = true;

    int row = stones[edge][0], col = stones[edge][1];

    for (auto [nextCol, j] : adjRow[row]) {
      if (visited[j]) {
        continue;
      }

      dfs(adjRow, adjCol, visited, j, stones);
    }

    for (auto [nextRow, j] : adjCol[col]) {
      if (visited[j]) {
        continue;
      }

      dfs(adjRow, adjCol, visited, j, stones);
    }
  }

public:
  int removeStones(vector<vector<int>> &stones) {
    int components = 0;

    AdjList adjRow, adjCol;
    for (int i = 0; i < stones.size(); i++) {
      adjRow[stones[i][0]].push_back({stones[i][1], i});
      adjCol[stones[i][1]].push_back({stones[i][0], i});
    }

    VisitedEdges visited(stones.size(), false);

    for (int i = 0; i < stones.size(); i++) {
      if (visited[i]) {
        continue;
      }

      dfs(adjRow, adjCol, visited, i, stones);
      ++components;
    }
    return stones.size() - components;
  }
};