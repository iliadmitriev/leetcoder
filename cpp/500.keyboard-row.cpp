#include <cctype>
#include <string>
#include <unordered_set>
#include <vector>

using std::string;
using std::unordered_set;
using std::vector;

class Solution {
private:
  bool inline isSubset(const unordered_set<char> &superSet, const string &s) {
    for (char c : s) {
      if (!superSet.count(tolower(c))) {
        return false;
      }
    }
    return true;
  }

public:
  vector<string> findWords(vector<string> &words) {
    unordered_set<char> rows[3] = {
        {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
        {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
        {'z', 'x', 'c', 'v', 'b', 'n', 'm'}};

    vector<string> res;

    for (string &word : words) {
      if (isSubset(rows[0], word) || isSubset(rows[1], word) ||
          isSubset(rows[2], word)) {
        res.push_back(word);
      }
    }

    return res;
  }
};