#include <ctime>
#include <iomanip>
#include <sstream>
#include <string>

using std::string;

class Solution {
public:
  string dayOfTheWeek(int day, int month, int year) {
    std::tm t;
    t.tm_year = year - 1900;
    t.tm_mon = month - 1;
    t.tm_mday = day;
    std::mktime(&t); // update time

    std::stringstream ss;
    ss << std::put_time(&t, "%A");

    return ss.str();
  }
};