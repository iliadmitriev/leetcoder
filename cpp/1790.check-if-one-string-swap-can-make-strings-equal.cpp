#include <string>

using std::string;

class Solution {
public:
  bool areAlmostEqual(string s1, string s2) {

    if (s1.size() != s2.size()) {
      return false;
    }

    const int N = s1.size();
    int swap = 2, ind = -1;

    for (int i = 0; i < N; i++) {
      if (s1[i] == s2[i]) {
        continue;
      }

      swap--;
      if (swap < 0) {
        return false;
      }

      if (ind >= 0 && (s1[ind] != s2[i] || s1[i] != s2[ind])) {
        return false;
      }

      ind = i;
    }

    return swap == 0 || swap == 2;
  }
};