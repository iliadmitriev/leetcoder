#include <bitset>
#include <string>

using std::string, std::bitset;

class Solution {
public:
  int canBeTypedWords(string text, string brokenLetters) {
    const int n = text.size();
    const size_t ALPHA = 26;
    const char BASE = 'a';
    const char SEP = ' ';
    std::bitset<ALPHA> broken;

    int j = 0;
    int count = 0;
    bool cur = false;

    for (char ch : brokenLetters) {
      broken[ch - BASE] = true;
    }

    for (int i = 0; i < n; i++) {
      if (text[i] != SEP) {
        cur |= broken[text[i] - BASE];
        continue;
      }

      if (j < i) {
        if (!cur) {
          count++;
        }
        j = i + 1;
        cur = false;
      }
    }

    if (j < n) {
      if (!cur) {
        count++;
      }
    }

    return count;
  }
};