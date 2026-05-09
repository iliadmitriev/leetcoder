class Solution {
private:
    const int MOD = 1e9 + 7;

public:
    int countHomogenous(string s) {
        long long total = 0;
        int cur = 0;
        char prev = '#';

        for (char ch: s) {
            if (ch != prev) {
                cur = 0;
            } 
            cur++;
            total += cur;
            prev = ch;
        }
        return total % MOD;
    }
};