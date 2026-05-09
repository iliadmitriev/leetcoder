#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  bool inline checkEngVowel(char ch) {
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
  }

public:
  int vowelStrings(vector<string> &words, int left, int right) {
    int counter = 0;

    for (int i = left; i <= right; ++i) {
      if (checkEngVowel(words[i].front()) && checkEngVowel(words[i].back()))
        counter++;
    }

    return counter;
  }
};