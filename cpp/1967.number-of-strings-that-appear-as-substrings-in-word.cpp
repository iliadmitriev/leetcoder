#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        auto check = [](const string& pat, const string& s) -> bool {
            return s.find(pat) != std::string::npos;
        };

        int res = 0;

        for (string& pat : patterns) {
            if (check(pat, word)) {
                res++;
            }
        }

        return res;
    }
};