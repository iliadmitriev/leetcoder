#include <string>

class Solution {
private:
    long long memoWav[20][11][11][2][2]; // ~10k x 8 byte
    long long memoCnt[20][11][11][2][2]; // ~10k x 8 byte
    bool vis[20][11][11][2][2];

    std::string s;

    struct Result {
        long long wav;
        long long cnt;
    };

    Result dfs(int index, int pprev, int prev, bool isLess, bool isStarted) {
        if (index == s.length()) {
            return {0, 1};
        }

        if (vis[index][pprev][prev][isLess][isStarted]) {
            return {
                memoWav[index][pprev][prev][isLess][isStarted],
                memoCnt[index][pprev][prev][isLess][isStarted],
            };
        }

        int limit = 9;
        if (!isLess) {
            limit = s[index] - '0';
        }

        long long totalWav = 0;
        long long totalCnt = 0;

        for (int d = 0; d <= limit; d++) {
            int nextLess = isLess || (d < limit);

            if (!isStarted) {
                if (d == 0) {
                    // case 1: continue leading zeros
                    Result res = dfs(index + 1, 10, 10, nextLess, 0);
                    totalWav += res.wav;
                    totalCnt += res.cnt;
                } else {
                    // case 2: place first significant non-zero digit
                    Result res = dfs(index + 1, 10, d, nextLess, 1);
                    totalWav += res.wav;
                    totalCnt += res.cnt;
                }
            } else {
                // case 3: continue building number
                int isWav = 0;
                if (pprev != 10 && prev != 10) {
                    isWav = ((pprev < prev) && (prev > d)) ||
                            ((pprev > prev) && (prev < d));
                }

                Result res = dfs(index + 1, prev, d, nextLess, 1);

                totalWav += res.wav;
                if (isWav) {
                    totalWav += res.cnt;
                }

                totalCnt += res.cnt;
            }
        }

        // cache result
        vis[index][pprev][prev][isLess][isStarted] = true;
        memoWav[index][pprev][prev][isLess][isStarted] = totalWav;
        memoCnt[index][pprev][prev][isLess][isStarted] = totalCnt;
        return {totalWav, totalCnt};
    }

    long long calc(long long num) {
        if (num < 100) {
            return 0;
        }

        s = std::to_string(num);

        // clear cache
        std::memset(vis, 0, sizeof(vis));

        Result res = dfs(0, 10, 10, 0, 0);
        return res.wav;
    }

public:
    long long totalWaviness(long long num1, long long num2) {
        return calc(num2) - calc(num1 - 1);
    }
};