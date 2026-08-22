class Solution {
public:
    bool checkDivisibility(int n) {
        int d, s = 0, p = 1, x = n;
        while (x) {
            d = x % 10;
            x /= 10;
            s += d;
            p *= d;
        }

        return n % (p + s) == 0;
    }
};