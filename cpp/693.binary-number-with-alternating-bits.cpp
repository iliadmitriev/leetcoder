class Solution {
public:
    bool hasAlternatingBits(int n) {
        int prev = 1 ^ n & 1;

        for (int x = n & 1; n; n >>= 1, x = n & 1) {
            if (prev == x) {
                return false;
            }

            prev = x;
        }

        return true;
    }
};