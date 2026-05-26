#include <array>

class Solution {
public:
    int numberOfSpecialChars(string word) {
        std::array<bool, 26> lower{false}, upper{false};
        int res = 0;

        for (char ch : word) {
          if ('a' <= ch && ch <= 'z') {
            lower[ch - 'a'] = true;
          } else {
            upper[ch - 'A'] = true;
        }
        }

        for (int i = 0; i < 26; i++) {
          res += (lower[i] && upper[i]);
        }

        return res;
    }
};