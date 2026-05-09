#include <queue>
#include <vector>

using std::vector, std::queue;

class Solution {
public:
  vector<int> eventualSafeNodes(vector<vector<int>> &graph) {
    const int N = graph.size();
    vector<vector<int>> revEdges(N);
    vector<int> outDegree(N, 0);
    vector<bool> safeNodes(N, false);
    queue<int> que;

    for (int i = 0; i < N; i++) {
      for (int j : graph[i]) {
        revEdges[j].push_back(i);
        outDegree[i]++;
      }

      if (!graph[i].size()) {
        que.push(i);
      }
    }

    while (que.size()) {
      int u = que.front();
      que.pop();
      safeNodes[u] = true;

      for (int v : revEdges[u]) {
        outDegree[v]--;
        if (outDegree[v] == 0) {
          que.push(v);
        }
      }
    }

    vector<int> safe;
    for (int i = 0; i < N; i++) {
      if (safeNodes[i]) {
        safe.push_back(i);
      }
    }

    return safe;
  }
};