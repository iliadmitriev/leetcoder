#include <ios>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using std::string, std::vector, std::stringstream;
const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  string addSpaces(string s, vector<int> &spaces) {
    const int n = s.size(), m = spaces.size();
    const int total = n + m;

    int i = 0, j = 0, k = 0;
    char res[total];

    while (i < n) {
      if (j < m && i == spaces[j]) {
        res[k++] = ' ';
        j++;
      }
      res[k++] = s[i++];
    }

    return string(res, total);
  }
};