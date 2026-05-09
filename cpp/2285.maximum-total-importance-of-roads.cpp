#include <algorithm>
#include <vector>
using std::sort;
using std::vector;

class Solution {
public:
  long long maximumImportance(int n, vector<vector<int>> &roads) {
    long long maxImportance = 0;
    vector<int> inDegree(n);

    for (int i = 0; i < roads.size(); i++) {
      inDegree[roads[i][0]]++;
      inDegree[roads[i][1]]++;
    }

    sort(inDegree.begin(), inDegree.end());

    for (int i = 0; i < n; i++) {
      maxImportance += long(i + 1) * inDegree[i];
    }

    return maxImportance;
  }
};