#include <queue>
#include <vector>

using std::pair;
using std::priority_queue;
using std::vector;

class Graph {
private:
  int _size;
  vector<vector<pair<int, int>>> _adj;

public:
  Graph(int n, vector<vector<int>> &edges) : _size(n), _adj(n) {
    for (auto const &edge : edges) {
      _adj[edge[0]].push_back({edge[1], edge[2]});
    }
  }

  void addEdge(vector<int> edge) {
    _adj[edge[0]].push_back({edge[1], edge[2]});
  }

  int shortestPath(int node1, int node2) {
    const int maxCost = int(10e7);

    vector<int> path(_size, maxCost);
    priority_queue<pair<int, int>, vector<pair<int, int>>, std::greater<>> pq;
    pq.push({0, node1});
    path[node1] = 0;

    while (pq.size()) {
      auto [dist, node] = pq.top();
      pq.pop();

      if (node == node2) {
        return dist;
      }

      for (auto [child, cost] : _adj[node]) {
        if (path[child] > dist + cost) {
          path[child] = dist + cost;
          pq.push({path[child], child});
        }
      }
    }

    return -1;
  }
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */