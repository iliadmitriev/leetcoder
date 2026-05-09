#include <cctype>
#include <sstream>
#include <string>

using std::string, std::stringstream;
class Solution {
public:
  string reformat(string s) {
    stringstream ss, letters, digits;

    for (char c : s) {
      if (std::isdigit(c)) {
        digits << c;
      } else {
        letters << c;
      }
    }

    int d = digits.tellp();
    int l = letters.tellp();

    if (d < l) {
      digits.swap(letters);
      std::swap(d, l);
    }

    if (d - l > 1) {
      return "";
    }

    char c;

    for (int i = 0; i < d + l; i++) {
      (i % 2 == 0 ? digits : letters) >> c;

      ss << c;
    }

    return ss.str();
  }
};