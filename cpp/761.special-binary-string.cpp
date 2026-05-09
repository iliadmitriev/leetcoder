#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
    string makeLargestSpecial(string s) {
        if (s.empty()) {
            return "";
        }

        vector<string> res;
        std::stringstream out;
        const int n = s.length();
        int count = 0;

        for (int i = 0, j = 0; j < n; j++) {
            if (s[j] == '1') {
                count++;
            } else {
                count--;
            }

            if (count == 0) {
                res.push_back("1" + makeLargestSpecial(s.substr(i + 1, j - i)) +
                              "0");
                i = j + 1;
            }
        }

        std::sort(res.begin(), res.end(), std::greater<string>());

        for (const string& a : res) {
            out << a;
        }

        return out.str();
    }
};