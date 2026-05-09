
#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

using std::pair;
using std::priority_queue;
using std::unordered_map;
using std::vector;

class Solution {
public:
  double maxProbability(int n, vector<vector<int>> &edges,
                        vector<double> &succProb, int start_node,
                        int end_node) {

    unordered_map<int, vector<pair<int, double>>> adj;

    for (int i = 0; i < edges.size(); i++) {
      adj[edges[i][0]].push_back({edges[i][1], succProb[i]});
      adj[edges[i][1]].push_back({edges[i][0], succProb[i]});
    }

    priority_queue<pair<double, int>, vector<pair<double, int>>, std::less<>>
        pq;

    pq.push({1.0, start_node});

    vector<double> prob(n, 0.0);
    prob[start_node] = 1.0;

    while (pq.size()) {
      auto [nodeProb, node] = pq.top();
      pq.pop();

      if (prob[node] > nodeProb) {
        continue;
      }

      for (auto [child, childProb] : adj[node]) {
        double newProb = nodeProb * childProb;

        if (prob[child] < newProb) {
          prob[child] = newProb;
          pq.push({newProb, child});
        }
      }
    }

    return prob[end_node];
  }
};
