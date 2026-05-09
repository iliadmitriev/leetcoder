class Solution {
public:
    int concatenatedBinary(int n) {
        const uint MOD = int(1e9) + 7;
        unsigned long long v = 0;
        uint shift = 0;

        for (uint i = 1; i <= n; i++) {
            if ((i & (i - 1)) == 0) {
                shift++;
            }
            
            v = (v << shift | i) % MOD;
        }

        return v;
    }
};