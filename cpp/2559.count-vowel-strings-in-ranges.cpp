#include <iostream>
#include <string>
#include <vector>

using std::vector, std::string;

static const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  vector<int> vowelStrings(vector<string> &words,
                           vector<vector<int>> &queries) {
    const size_t n = words.size(), m = queries.size();
    vector<int> res(m, 0);
    vector<int> cache(n + 1, 0);

    for (int i = 1; i <= n; i++) {
      cache[i] = cache[i - 1] +
                 (isVowel(words[i - 1][0]) && isVowel(words[i - 1].back()));
    }

    for (int j = 0; j < m; j++) {
      int l = queries[j][0], r = queries[j][1];
      res[j] = cache[r + 1] - cache[l];
    }

    return res;
  }

private:
  inline bool isVowel(char ch) {
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
  }
};