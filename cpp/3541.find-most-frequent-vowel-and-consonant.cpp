
#define ALPHABET 26

#include <array>
#include <string>

using std::array, std::string;

class Solution {
private:
  bool inline isVowel(int c) {
    return c == 0 || c == 4 || c == 8 || c == 14 || c == 20;
  }

public:
  int maxFreqSum(string s) {
    array<int, ALPHABET> cnt = {};
    const char base = 'a';
    int maxVowel = 0, maxConsonant = 0;

    for (char ch : s) {
      cnt[ch - base]++;
    }

    for (int i = 0; i < ALPHABET; i++) {
      if (isVowel(i)) {
        maxVowel = std::max(maxVowel, cnt[i]);
      } else {
        maxConsonant = std::max(maxConsonant, cnt[i]);
      }
    }

    return maxVowel + maxConsonant;
  }
};