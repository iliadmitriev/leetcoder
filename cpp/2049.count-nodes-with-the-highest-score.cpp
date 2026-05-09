#include <vector>

using std::max;
using std::vector;

class Solution {
private:
  int dfs(const vector<vector<int>> &adj, int par, vector<int> &child) {
    child[par] = 1;
    for (int ch : adj[par]) {
      child[par] += dfs(adj, ch, child);
    }

    return child[par];
  }

public:
  int countHighestScoreNodes(vector<int> &parents) {
    int n = parents.size();
    vector<int> inorder(n, 0);
    vector<vector<int>> adj(n);

    for (int i = 1; i < n; ++i) {
      adj[parents[i]].push_back(i);
      inorder[parents[i]]++;
    }

    vector<int> child(n, 0);
    child[0] = dfs(adj, 0, child);

    long maxScore = 0;
    int maxCount = 0;

    for (int i = 0; i < n; ++i) {
      long val = max(1, n - child[i]);
      for (int j : adj[i]) {
        val *= child[j];
      }

      if (val > maxScore) {
        maxScore = val;
        maxCount = 1;
      } else if (val == maxScore) {
        maxCount++;
      }
    }

    return maxCount;
  }
};