class Solution {
public:
    int rotatedDigits(int n) {
        // 3,4,7 - digits invalidate number
        // 2,5,6,9 - digits change number
        // 0,1,8 - digits do nothing (just ignore them)

        const int N = 12;                   // max decimal digits
        const int D = 2;                    // max boolean states
        const string S = std::to_string(n); // easier to iterate a string

        // memoization: memo[digit position, is closed, changed],
        // -1 - not calculated yet
        vector<vector<vector<int>>> memo(
            N, vector<vector<int>>(D, vector<int>(D, -1)));

        auto dp = [&S, &memo](auto&& self, int i, bool closed,
                              bool changed) -> int {
            if (i == S.size()) {
                return changed;
            }

            if (memo[i][closed][changed] != -1) {
                return memo[i][closed][changed];
            }

            int res = 0; // accumulator

            int limit = closed ? S[i] - '0' : 9;

            for (int d = 0; d <= limit; d++) {
                if (d == 3 || d == 4 || d == 7) {
                    continue;
                }

                bool to_change =
                    changed || d == 2 || d == 5 || d == 6 || d == 9;
                bool to_close = closed && d == limit;

                res += self(self, i + 1, to_close, to_change);
            }

            return memo[i][closed][changed] = res;
        };

        return dp(dp, 0, true, false);
    }
};