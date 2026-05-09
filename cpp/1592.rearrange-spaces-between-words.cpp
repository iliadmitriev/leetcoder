#include <sstream>
#include <string>
#include <vector>

using std::string, std::vector, std::ostringstream;

class Solution {
public:
  string reorderSpaces(string text) {
    const int n = text.size();
    int spaces = 0;
    vector<string> words;
    ostringstream oss;

    int j = 0;
    for (int i = 0; i < n; i++) {
      if (text[i] != ' ') {
        continue;
      }

      spaces++;

      if (i - j > 0) {
        words.push_back(text.substr(j, i - j));
      }

      j = i + 1;
    }

    if (j < n) {
      words.push_back(text.substr(j));
    }

    int slots = words.size() - 1;

    if (slots == 0) {
      return words[0] + string(spaces, ' ');
    }

    string sep = string(spaces / slots, ' '), end = string(spaces % slots, ' ');

    oss << words.front();

    for (int i = 1; i < words.size(); i++) {
      oss << sep << words[i];
    }

    oss << end;

    return oss.str();
  }
};