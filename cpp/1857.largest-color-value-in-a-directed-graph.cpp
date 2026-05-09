#include <queue>
#include <string>
#include <unordered_map>
#include <vector>

using std::string, std::vector, std::unordered_map, std::queue;

class Solution {
public:
  int largestPathValue(string colors, vector<vector<int>> &edges) {
    const int n = colors.size();
    int visited = 0;
    int maxColors = 0;
    vector<vector<int>> invAdj(n); /// inverted adjacency list
    vector<int> inDegree(n, 0);
    vector<unordered_map<char, int>> colorCount(n);
    queue<int> q;

    for (const auto &edge : edges) {
      invAdj[edge[1]].push_back(edge[0]);
      inDegree[edge[0]]++;
    }

    for (int i = 0; i < n; i++) {
      if (inDegree[i] == 0) {
        q.push(i);
      }
    }

    while (!q.empty()) {
      int node = q.front();
      q.pop();
      visited++;
      colorCount[node][colors[node]]++;
      maxColors = std::max(maxColors, colorCount[node][colors[node]]);

      for (int next : invAdj[node]) {
        for (const auto &[color, count] : colorCount[node]) {
          colorCount[next][color] = std::max(colorCount[next][color], count);
        }

        inDegree[next]--;
        if (inDegree[next] == 0) {
          q.push(next);
        }
      }
    }

    if (visited < n) {
      return -1;
    }

    return maxColors;
  }
};