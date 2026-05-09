#include <iostream>
#include <string>
#include <vector>

using std::string, std::vector;

static auto fast = []() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return nullptr;
}();

class Solution {
public:
  string shiftingLetters(string s, vector<vector<int>> &shifts) {
    const size_t N = s.size();
    const int _base = 26;
    const int _bias = 'a';

    vector<int> prefix(N + 1, 0);

    for (const vector<int> &sh : shifts) {
      int dir = 2 * sh[2] - 1, start = sh[0], end = sh[1] + 1;

      prefix[start] += dir;
      prefix[end] -= dir;
    }

    int cur = 0;
    for (int i = 0; i < N; i++) {
      cur += prefix[i];
      cur %= _base;
      s[i] = _bias + (s[i] - _bias + cur + _base) % _base;
    }

    return s;
  }
};
