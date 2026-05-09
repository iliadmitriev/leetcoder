#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

using std::sort;
using std::string;
using std::unordered_set;
using std::vector;

class Solution {
public:
  string longestWord(vector<string> &words) {
    sort(words.begin(), words.end(), [](const string &a, const string &b) {
      if (a.length() == b.length())
        return a > b;

      return a.length() < b.length();
    });

    unordered_set<string> cache;
    cache.insert("");

    string res = "";
    for (const auto &word : words) {
      if (cache.count(word.substr(0, word.length() - 1))) {
        cache.insert(word);
        res = word;
      }
    }

    return res;
  }
};