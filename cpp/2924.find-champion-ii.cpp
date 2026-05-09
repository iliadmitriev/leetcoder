#include <vector>
using std::vector;

class Solution {
public:
  int findChampion(int n, vector<vector<int>> &edges) {
    vector<int> inorder(n, 0);
    int m = edges.size();
    for (int i = 0; i < m; i++) {
      inorder[edges[i][1]]++;
    }

    int candidate = -1;
    for (int u = 0; u < n; u++) {
      if (inorder[u]) {
        continue;
      }

      if (candidate == -1) {
        candidate = u;
      } else {
        return -1;
      }
    }

    return candidate;
  }
};