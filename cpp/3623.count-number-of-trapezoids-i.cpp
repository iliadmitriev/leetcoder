#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
public:
  int countTrapezoids(vector<vector<int>> &points) {
    const int MOD = 1e9 + 7;

    // count the number of points on each line parallel to x axis
    unordered_map<int, int> cnt;
    for (const auto &point : points) {
      cnt[point[1]]++;
    }

    long long res = 0;
    long long total = 0;

    for (auto [_, v] : cnt) {
      long long edges = 1LL * v * (v - 1) / 2;

      res += edges * total;
      res %= MOD;

      total += edges;
      total %= MOD;
    }

    return res;
  }
};