#include <ctime>
#include <string>

using std::string;

class Solution {
public:
  int dayOfYear(string date) {
    std::tm t;
    strptime(date.c_str(), "%Y-%m-%d", &t);

    std::time_t t1 = std::mktime(&t);
    t.tm_mday = 0;
    t.tm_mon = 0;
    std::time_t t2 = std::mktime(&t);

    return (t1 - t2) / 86400;
  }
};