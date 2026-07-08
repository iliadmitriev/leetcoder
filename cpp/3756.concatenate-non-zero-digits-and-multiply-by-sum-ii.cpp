#include <string>
#include <vector>

using std::string, std::vector;

static const int MOD = 1e9 + 7;
static const int MAX_SZ = 1e5 + 1;
long long POW10[MAX_SZ];

int init = []() {
    POW10[0] = 1; // 10^0 = 1

    for (int i = 1; i < MAX_SZ; i++) {
        POW10[i] = POW10[i - 1] * 10 % MOD;
    }

    return 0;
}();

class Solution {
public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        const int n = s.size();
        const int m = queries.size();

        vector<int> sum(n + 1, 0);
        vector<long long> p(n + 1, 0LL);
        vector<int> cnt(n + 1, 0);
        vector<int> res(m, 0);

        for (int i = 0; i < n; i++) {
            int d = s[i] - '0';

            sum[i + 1] = sum[i] + d;

            if (d) { // if d is not 0
                p[i + 1] = (p[i] * 10 + d) % MOD;
                cnt[i + 1] = cnt[i] + 1;

            } else { // if d is 0, skip
                p[i + 1] = p[i];
                cnt[i + 1] = cnt[i];
            }
        }

        for (int j = 0; j < m; j++) {
            int l = queries[j][0], r = queries[j][1] + 1; // not inclusive

            int len = cnt[r] - cnt[l]; // number of non-zeroes in [l, r)
            // p[r] = p[l] * (10 ^ len) + x
            // x = p[r] - p[l] * (10 ^ len)
            long long x = (MOD + p[r] - p[l] * POW10[len] % MOD) % MOD;
            long long z = sum[r] - sum[l];

            res[j] = x * z % MOD;
        }

        return res;
    }
};