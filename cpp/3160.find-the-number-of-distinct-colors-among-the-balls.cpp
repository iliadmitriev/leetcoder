#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
public:
  vector<int> queryResults(int limit, vector<vector<int>> &queries) {
    const int N = queries.size();
    vector<int> res(N);
    unordered_map<int, int> colors, balls;

    for (int i = 0; i < N; ++i) {
      const int ball = queries[i][0], color = queries[i][1];

      int prevColor = balls[ball];
      balls[ball] = color;

      colors[color]++;

      if (prevColor > 0) {
        colors[prevColor]--;

        if (colors[prevColor] == 0) {
          colors.erase(prevColor);
        }
      }

      res[i] = colors.size();
    }

    return res;
  }
};