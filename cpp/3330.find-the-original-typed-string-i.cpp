#include <string>
using std::string;

class Solution {
public:
  int possibleStringCount(string word) {
    int total = 1;
    char prev = 0;

    for (char ch : word) {
      if (prev == ch) {
        total++;
      }
      prev = ch;
    }

    return total;
  }
};