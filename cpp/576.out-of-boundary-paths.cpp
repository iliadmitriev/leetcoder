
class Solution {

public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        map<tuple<int,int,int>, int> cache;
        const int MOD = 1e9 + 7;

        std::function<int(int,int,int)> dp;

        dp = [&dp, MOD, n, m, &cache](int row, int col, int moves) -> int {
            if (row < 0 || row >= m || col < 0 || col >= n) {
                return 1;
            }

            if (moves == 0) {
                return 0;
            }

            tuple<int,int,int> key = {row, col, moves};
            if (cache.find(key) != cache.end()) {
                return cache[key];
            }

            long res = 0;

            res += dp(row - 1, col, moves - 1) % MOD;
            res += dp(row + 1, col, moves - 1) % MOD;
            res += dp(row, col - 1, moves - 1) % MOD;
            res += dp(row, col + 1, moves - 1) % MOD;
            
            return cache[key] = res % MOD;
        };

        return dp(startRow, startColumn, maxMove);
    }
};