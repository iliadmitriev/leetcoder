#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
using std::string, std::stringstream;

const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  int isPrefixOfWord(string sentence, string searchWord) {
    int pos = 1;

    stringstream ss(sentence);
    string word;

    while (std::getline(ss, word, ' ')) {
      if (word.size() >= searchWord.size() &&
          word.compare(0, searchWord.size(), searchWord) == 0) {
        return pos;
      }

      pos++;
    }

    return -1;
  }
};