#include <queue>
#include <vector>

using std::vector, std::queue, std::max;
class Solution {
public:
  int maximumInvitations(vector<int> &favorite) {
    const int N = favorite.size();
    vector<int> inDegree(N, 0);
    vector<int> depth(N, 1);

    for (int i = 0; i < N; i++) {
      inDegree[favorite[i]]++;
    }

    queue<int> q;
    for (int node = 0; node < N; node++) {
      if (inDegree[node] == 0) {
        q.push(node);
      }
    }

    while (q.size()) {
      int node = q.front();
      q.pop();
      int nnode = favorite[node];
      depth[nnode] = max(depth[nnode], depth[node] + 1);

      inDegree[nnode]--;
      if (inDegree[nnode] == 0) {
        q.push(nnode);
      }
    }

    int maxCycleLen = 0, maxTwoCyclePath = 0;

    for (int node = 0; node < N; node++) {
      if (inDegree[node] == 0) {
        continue;
      }

      int cycleLen = 0;
      int cur = node;
      while (inDegree[cur] != 0) {
        inDegree[cur] = 0;
        cur = favorite[cur];
        cycleLen++;
      }

      if (cycleLen == 2) {
        maxTwoCyclePath += depth[node] + depth[favorite[node]];
      } else {
        maxCycleLen = max(maxCycleLen, cycleLen);
      }
    }

    return max(maxCycleLen, maxTwoCyclePath);
  }
};