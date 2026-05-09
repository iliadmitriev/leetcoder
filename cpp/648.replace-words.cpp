#include <algorithm>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  string replaceWords(vector<string> &dictionary, string sentence) {
    stringstream result;
    std::set<string> dictSet;
    int minLen = numeric_limits<int>::max(),
        maxLen = numeric_limits<int>::min();

    for (auto &word : dictionary) {
      dictSet.insert(word);
      minLen = min(minLen, (int)word.size());
      maxLen = max(maxLen, (int)word.size());
    }

    istringstream in(sentence);
    for (string word; getline(in, word, ' ');) {
      bool replaced = false;
      for (int i = minLen; i <= maxLen; ++i) {
        if (dictSet.count(word.substr(0, i))) {
          result << (result.tellp() ? " " : "") << word.substr(0, i);
          replaced = true;
          break;
        }
      }

      if (!replaced)
        result << (result.tellp() ? " " : "") << word;
    }

    return result.str();
  }
};