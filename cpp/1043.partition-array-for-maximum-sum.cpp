class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size();
        vector<int> cache(n, -1);

        std::function<int(int)> dp;
        dp = [&dp, &cache, &arr, n, k] (int i) -> int {
            if (i >= n) {
                return 0;
            }

            if (cache[i] != -1) {
                return cache[i];
            }

            int res = 0;
            int curMax = 0;

            for (int j = i; j < min(n, i + k); j++) {
                curMax = max(curMax, arr[j]);
                res = max(res, curMax * (j - i + 1) + dp(j + 1));
            }

            return cache[i] = res;
        };

        return dp(0);
    }
};