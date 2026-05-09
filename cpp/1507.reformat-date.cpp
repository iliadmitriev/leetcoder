#include <iomanip>
#include <sstream>
#include <string>

using std::string;

class Solution {
public:
  string reformatDate(string date) {
    int j = 0;
    while (std::isdigit(date[j]) && j < date.size()) {
      j++;
    }

    string format{"%d" + date.substr(j, 2) + " %b %Y"};
    std::tm tm;

    std::istringstream is(date);
    is >> std::get_time(&tm, format.c_str());

    std::ostringstream os;
    os << std::put_time(&tm, "%Y-%m-%d");

    return os.str();
  }
};