#include <ctime>
#include <string>
using std::string;

class Solution {
public:
  int daysBetweenDates(string date1, string date2) {
    std::tm d1, d2;

    strptime(date1.c_str(), "%Y-%m-%d", &d1);
    strptime(date2.c_str(), "%Y-%m-%d", &d2);

    std::time_t t1 = std::mktime(&d1);
    std::time_t t2 = std::mktime(&d2);

    if (t1 > t2) {
      std::swap(t1, t2);
    }

    return std::difftime(t2, t1) / 86400;
  }
};