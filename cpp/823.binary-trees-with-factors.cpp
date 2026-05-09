const int MOD = int(1e9) + 7;

class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        std::sort(arr.begin(), arr.end());
        
        // base case:
        unordered_map<int, long> dp;
        for (int i = 0; i < arr.size(); i++) {
            dp[arr[i]] = 1;
        }

        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < arr.size(); j++) {
                int a = arr[i] / arr[j];
                int b = arr[i] % arr[j];
                if (a == 0) {
                    break;
                }

                if (b == 0 && dp.find(a) != dp.end()) {
                    dp[arr[i]] += dp[a] * dp[arr[j]];
                    dp[arr[i]] %= MOD;
                }
            }
        }

        int res = 0;
        for (auto [_, v] : dp) {
            res += v;
            res %= MOD;
        }
        return res;
    }
};