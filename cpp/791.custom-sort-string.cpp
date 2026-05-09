#include <sstream>
class Solution {
public:
  string customSortString(string order, string s) {
    map<char, int> m;
    std::stringstream ss;

    for (auto c : s) {
      m[c]++;
    }

    for (auto o : order) {
      while (m[o]) {
        ss << o;
        m[o]--;
      }
      m.erase(o);
    }

    for (auto [k, v] : m) {
      while (v) {
        ss << k;
        v--;
      }
    }

    return ss.str();
  }
};