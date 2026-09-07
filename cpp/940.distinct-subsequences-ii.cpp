#include <array>
#include <string>

using std::string;

class Solution {
public:
    int distinctSubseqII(string s) {
        const int n = s.size();
        const char base = 'a';
        const int mod = int(1e9) + 7;

        std::array<int, 26> last = {0};
        long dp = 1;
        int prev;

        for (int i = 0; i < n; i++) {
            prev = dp;
            dp *= 2;

            dp -= last[s[i] - base];
            dp += mod;
            dp %= mod;

            last[s[i] - base] = prev;
        }

        return (dp + mod - 1) % mod;
    }
};