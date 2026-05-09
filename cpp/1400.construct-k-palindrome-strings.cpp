#include <array>
#include <iostream>
#include <numeric>
#include <string>

using std::array, std::string;

static const auto ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  bool canConstruct(string s, int k) {
    if (s.size() < k) {
      return false;
    }

    if (s.size() == k) {
      return true;
    }

    array<int, 26> count{};
    for (auto c : s) {
      ++count[c - 'a'];
    }

    int odd = std::accumulate(count.begin(), count.end(), 0,
                              [](int res, int v) { return res + v % 2; });

    return odd <= k;
  }
};