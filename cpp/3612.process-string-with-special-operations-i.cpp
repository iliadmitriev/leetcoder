#include <algorithm>
#include <string>

using std::string;

class Solution {
public:
    string processStr(string s) {
        string res;
        // # - duplicate
        // % - reverse
        // * - pop last if exists

        for (char ch : s) {
            if (ch == '#') {
                res.append(res);
            } else if (ch == '%') {
                std::reverse(res.begin(), res.end());
            } else if (ch == '*') {
                if (res.size()) {
                    res.pop_back();
                }
            } else {
                res.push_back(ch);
            }
        }

        return res;
    }
};