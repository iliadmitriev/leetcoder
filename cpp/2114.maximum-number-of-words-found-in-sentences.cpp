#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  int countWords(string &sentence) {
    int words = 1;

    for (auto c : sentence)
      if (c == ' ')
        words++;

    return words;
  }

public:
  int mostWordsFound(vector<string> &sentences) {
    int maxWords = 0;
    for (string &s : sentences) {
      maxWords = std::max(maxWords, countWords(s));
    }

    return maxWords;
  }
};