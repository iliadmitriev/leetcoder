#include <algorithm>
#include <iostream>
#include <string>

using std::string;

static const int ZERO = []() {
  std::cin.tie(nullptr);
  std::ios_base::sync_with_stdio(false);
  return 0;
}();

class Solution {
public:
  int maxScore(string s) {

    int maxScore = 0, score = std::count_if(s.begin(), s.end(),
                                            [](char c) { return c == '1'; });

    for (int i = 0; i < s.size() - 1; ++i) {
      if (s[i] == '0') {
        ++score;
      } else {
        --score;
      }

      maxScore = std::max(maxScore, score);
    }

    return maxScore;
  }
};