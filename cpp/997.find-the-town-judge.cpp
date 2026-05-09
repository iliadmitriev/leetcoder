
class Solution {
public:
  int findJudge(int n, vector<vector<int>> &trust) {
    vector<int> order(n + 1, 0);

    for (const auto &tr : trust) {
      order[tr[0]]--;
      order[tr[1]]++;
    }

    for (int i = 1; i <= n; i++) {
      if (order[i] == n - 1) {
        return i;
      }
    }

    return -1;
  }
};