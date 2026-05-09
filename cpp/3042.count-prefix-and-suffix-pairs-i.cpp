#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

static const auto io_sync_off = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
private:
  bool isPrefixAndSuffix(const string &t, const string &s) {
    int m = s.size(), n = t.size();
    return m >= n && s.compare(0, n, t) == 0 && s.compare(m - n, n, t) == 0;
  }

public:
  int countPrefixSuffixPairs(vector<string> &words) {
    int count = 0, n = words.size();

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        if (isPrefixAndSuffix(words[i], words[j])) {
          count++;
        }
      }
    }

    return count;
  }
};