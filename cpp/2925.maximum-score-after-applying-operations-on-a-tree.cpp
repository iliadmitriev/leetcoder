class Solution {
private:
  long long dfs(const vector<vector<int>> &adj, const vector<int> &values,
                int node, int parent) {
    if (adj[node].size() == 1 && parent != -1) {
      return long(values[node]);
    }

    long long maxScore = 0;
    for (int next : adj[node]) {
      if (next != parent) {
        maxScore += dfs(adj, values, next, node);
      }
    }

    return min(maxScore, 0LL + values[node]);
  }

public:
  long long maximumScoreAfterOperations(vector<vector<int>> &edges,
                                        vector<int> &values) {
    vector<vector<int>> adj = vector<vector<int>>(values.size());

    for (const auto &edge : edges) {
      adj[edge[0]].push_back(edge[1]);
      adj[edge[1]].push_back(edge[0]);
    }

    return accumulate(values.begin(), values.end(), 0LL) -
           dfs(adj, values, 0, -1);
  }
};