#include <array>
#include <iostream>
#include <string>

using std::array, std::string;

const static int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  int minimumLength(string s) {
    array<int, 26> count{};
    for (auto c : s) {
      ++count[c - 'a'];
    }

    int res = 0;
    for (auto v : count) {
      res += 1 + (v - 1) % 2;
    }

    return res;
  }
};