#include <string>
#include <unordered_map>
#include <vector>

using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
  int countWords(vector<string> &words1, vector<string> &words2) {
    unordered_map<string, int> m1;
    unordered_map<string, int> m2;

    for (string &w : words1) {
      ++m1[w];
    }

    for (string &w : words2) {
      ++m2[w];
    }

    int res = 0;

    for (string &w : words1) {
      if (m1[w] == 1 && m2[w] == 1) {
        ++res;
        m1[w] = 0;
        m2[w] = 0;
      }
    }

    for (string &w : words2) {
      if (m1[w] == 1 && m2[w] == 1) {
        ++res;
      }
    }

    return res;
  }
};