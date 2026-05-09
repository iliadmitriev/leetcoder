#include <algorithm>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  int minimumPushes(string word) {
    vector<int> freq(26, 0);
    for (char c : word) {
      freq[c - 'a']++;
    }

    std::sort(freq.begin(), freq.end(), std::greater<int>());
    int res = 0;

    for (int i = 0; i < 26; i++) {
      res += (i / 8 + 1) * freq[i];
    }

    return res;
  }
};