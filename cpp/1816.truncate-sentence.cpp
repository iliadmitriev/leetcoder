#include <string>

using std::string;

class Solution {
public:
  string truncateSentence(string s, int k) {
    int words = 0;
    int cut = s.size();

    for (int i = 0; i < s.size(); i++) {
      if (s[i] == ' ') {
        words++;
      }

      if (words == k) {
        cut = i;
        break;
      }
    }

    return s.substr(0, cut);
  }
};