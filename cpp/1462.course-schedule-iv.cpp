#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using std::vector, std::unordered_map, std::unordered_set, std::queue;
class Solution {
public:
  vector<bool> checkIfPrerequisite(int numCourses,
                                   vector<vector<int>> &prerequisites,
                                   vector<vector<int>> &queries) {
    const int n = queries.size();
    vector<bool> res(n, false);
    vector<vector<int>> adj(numCourses);
    vector<int> inDegree(numCourses, 0);
    unordered_map<int, unordered_set<int>> pre;
    queue<int> q;

    for (const auto &edge : prerequisites) {
      adj[edge[0]].push_back(edge[1]);
      inDegree[edge[1]]++;
    }

    for (int i = 0; i < numCourses; i++) {
      if (inDegree[i] == 0) {
        q.push(i);
      }
    }

    while (!q.empty()) {
      int node = q.front();
      q.pop();

      for (int nnode : adj[node]) {
        pre[nnode].insert(node);
        for (auto v : pre[node]) {
          pre[nnode].insert(v);
        }

        inDegree[nnode]--;
        if (inDegree[nnode] == 0) {
          q.push(nnode);
        }
      }
    }

    for (int i = 0; i < n; i++) {
      res[i] = pre[queries[i][1]].count(queries[i][0]) > 0;
    }

    return res;
  }
};