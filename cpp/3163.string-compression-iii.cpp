#include <sstream>
#include <string>
using std::string;
class Solution {
public:
  string compressedString(string word) {
    char prev = 0;
    int counter = 0;
    std::stringstream res;

    for (char ch : word) {
      if (prev == ch && counter < 9) {
        counter++;
      } else {
        if (prev != 0) {
          res << counter;
          res << prev;
        }

        counter = 1;
      }

      prev = ch;
    }

    if (prev != 0) {
      res << counter;
      res << prev;
    }

    return res.str();
  }
};