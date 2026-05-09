#include <string>
using std::string;

class Solution {
private:
  inline bool match(char c) {
    return ('a' <= c && c <= 'z') || ('0' <= c && c <= '9');
  }

  inline bool isConsonant(char c) {
    return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' &&
           'a' <= c && c <= 'z';
  }

  inline bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
  }

public:
  bool isValid(string word) {
    if (word.size() < 3) {
      return false;
    }

    bool hasConsonant = false, hasVowel = false;

    for (char c : word) {
      char w = tolower(c);

      if (!match(w)) {
        return false;
      }

      if (isConsonant(w)) {
        hasConsonant = true;
      } else if (isVowel(w)) {
        hasVowel = true;
      }
    }

    return hasConsonant && hasVowel;
  }
};