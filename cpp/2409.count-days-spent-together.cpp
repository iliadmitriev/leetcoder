#include <ctime>
#include <string>

using std::string;

class Solution {
private:
    static constexpr const char* fmt = "%m-%d";
    int dayOfYear(const string& s) {
        struct tm base = {};
        strptime(s.c_str(), fmt, &base);
        
        std::mktime(&base);
        return base.tm_yday;
    }
public:
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int arrive = std::max(dayOfYear(arriveAlice), dayOfYear(arriveBob));
        int leave = std::min(dayOfYear(leaveAlice), dayOfYear(leaveBob)) + 1;
        
        return std::max(0, leave - arrive);
    }
};