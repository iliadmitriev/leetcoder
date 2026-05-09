#include <queue>
#include <vector>

using std::queue;
using std::vector;

class Solution {
private:
  bool topoSort(int n, const vector<vector<int>> &edges, vector<int> &arr) {
    vector<vector<int>> adj(n);
    vector<int> indegree(n, 0);

    for (const auto e : edges) {
      adj[e[0] - 1].push_back(e[1] - 1);
      indegree[e[1] - 1]++;
    }

    queue<int> q;
    int j = 0;
    for (int i = 0; i < n; ++i) {
      if (indegree[i] == 0) {
        q.push(i);
      }

      while (q.size()) {
        int u = q.front();
        q.pop();
        arr[u] = j++;

        for (int v : adj[u]) {
          indegree[v]--;
          if (indegree[v] == 0) {
            indegree[v] = -1;
            q.push(v);
          }
        }
      }
    }

    if (j != n) {
      return false;
    }

    return true;
  }

public:
  vector<vector<int>> buildMatrix(int k, vector<vector<int>> &rowConditions,
                                  vector<vector<int>> &colConditions) {
    vector<int> rows(k, 0), cols(k, 0);
    bool rowOk = topoSort(k, rowConditions, rows),
         colOk = topoSort(k, colConditions, cols);

    if (!rowOk || !colOk) {
      return {};
    }

    vector<vector<int>> ret(k, vector<int>(k, 0));
    int j = 0;
    for (int i = 0; i < k; ++i) {
      ret[rows[i]][cols[i]] = ++j;
    }

    return ret;
  }
};