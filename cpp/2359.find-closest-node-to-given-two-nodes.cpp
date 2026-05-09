#include <vector>
using std::vector;

class Solution {
private:
  vector<int> dfs(const vector<int> &edges, int node) {
    vector<int> distances(edges.size(), -1);
    int dist = 0;
    distances[node] = dist;

    while (edges[node] != -1 && distances[edges[node]] == -1) {
      dist++;
      node = edges[node];
      distances[node] = dist;
    }

    return distances;
  }

public:
  int closestMeetingNode(vector<int> &edges, int node1, int node2) {
    vector<int> distances1 = dfs(edges, node1);
    vector<int> distances2 = dfs(edges, node2);

    int minDist = edges.size();
    int minNode = -1;

    for (int i = 0; i < distances1.size(); i++) {
      if (distances1[i] == -1 || distances2[i] == -1) {
        continue;
      }

      int dist = std::max(distances1[i], distances2[i]);
      if (dist < minDist) {
        minDist = dist;
        minNode = i;
      }
    }

    return minNode;
  }
};