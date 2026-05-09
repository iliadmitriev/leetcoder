#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  vector<string> splitBySeparator(string &s, char separator) {
    vector<string> res;
    int i = 0, j = 0;

    while (j < s.size()) {
      j = i;
      while (j < s.size() && s[j] != separator)
        j++;

      if (j - i)
        res.push_back(s.substr(i, j - i));

      i = j + 1;
    }

    return res;
  }

public:
  vector<string> splitWordsBySeparator(vector<string> &words, char separator) {
    vector<string> res;
    for (string &word : words) {
      for (string &chunk : splitBySeparator(word, separator)) {
        res.push_back(chunk);
      }
    }

    return res;
  }
};