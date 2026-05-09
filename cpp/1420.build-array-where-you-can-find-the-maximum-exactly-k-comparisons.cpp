const int MOD = int(1e9) + 7;

class Solution {
public:
    int numOfArrays(int n, int m, int k) {
        
        // init dp memoization cache
        vector<vector<vector<int> > > cache(n + 1, vector<vector<int> >(m + 1, vector<int>(k + 1, -1)));
        // base case
        for (int curMax = 0; curMax <= m; curMax++) {
            cache[n][curMax][0] = 1;
        }

        // recurrent lambda function
        std::function<int(int, int, int)> dp;
        dp = [&](int i, int curMax, int remain) -> int {
            if (i == n) {
                return int(remain == 0);
            }
            if (remain < 0) {
                return 0;
            }
            // check cache;
            if (cache[i][curMax][remain] != -1) {
                return cache[i][curMax][remain];
            }
            int res = long(dp(i + 1, curMax, remain)) * curMax % MOD;

            for (int j = curMax + 1; j <= m; j++) {
                res = (res + dp(i + 1, j, remain - 1)) % MOD;
            }
            return cache[i][curMax][remain] = res;
        };

        return dp(0, 0, k);
    }
};