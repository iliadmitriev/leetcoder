#include <sstream>
#include <string>
using std::string;

class Solution {
public:
  string defangIPaddr(string address) {
    std::ostringstream oss;

    for (char c : address) {
      if (c == '.') {
        oss << "[.]";
      } else {
        oss << c;
      }
    }

    return oss.str();
  }
};