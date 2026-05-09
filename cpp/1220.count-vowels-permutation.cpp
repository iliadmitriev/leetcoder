const int MOD = int(1e9) + 7;

class Solution {
public:
    int countVowelPermutation(int n) {

        // 0 - empty symbol
        // 1 - 'a'
        // 2 - 'e'
        // 3 - 'i'
        // 4 - 'o'
        // 5 - 'u'
        vector<vector<char>> mp = {
            {1, 2, 3, 4, 5},  // 0
            {2},              // 1
            {1, 3},           // 2
            {1, 2, 4, 5},     // 3
            {3, 5},           // 4
            {1}               // 5
        };

        // range of alphabet from 0 to 5 = 6 symbols
        // we anly need two iterations of calcualtions current and previous
        // we will adress them as 
        // previous: (i - 1) % 2
        // current: i % 2
        vector<vector<int>> dp(2, vector<int>(6, -1));
        // base case: there is only one combination with one letter
        for (int j = 0; j < 6; j++) {
            dp[0][j] = 1;
        }

        for (int i = 1; i <= n; i++) {
            for (int cur = 0; cur < 6; cur++) {
                int cnt = 0;
                for (auto child : mp[cur]) {
                    cnt = (cnt + dp[(i - 1) % 2][child]) % MOD;
                }
                dp[i % 2][cur] = cnt;
            }
        }

        return dp[n % 2][0];
    }
};