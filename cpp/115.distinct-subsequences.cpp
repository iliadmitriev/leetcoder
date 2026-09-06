#include <sstream>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

using std::string, std::vector, std::unordered_set;

class Solution {
public:
    int numDistinct(string s, string t) {
        // rebuild the given source string s of
        // the characters met in the target string t
        unordered_set<char> tt(t.begin(), t.end());
        std::stringstream ss;

        for (char ch : s) {
            if (tt.count(ch)) {
                ss << ch;
            }
        }

        s = ss.str();
        const int m = s.size(), n = t.size();

        // if it's not enough characters in the source string
        const int diff = m - n;
        if (diff < 0) {
            return 0;
        }

        vector<long> dp(n + 1, 0);
        dp[n] = 1; // base case when collected the target of size n

        for (int i = m - 1; i >= 0; i--) {
            int start = std::max(0, i - diff); // clip bottom to 0
            int end = std::min(n, i + 1);      // clip top to n

            for (int j = start; j < end; j++) {
                if (s[i] == t[j]) {
                    dp[j] += dp[j + 1];
                }
            }
        }

        return dp[0];
    }
};