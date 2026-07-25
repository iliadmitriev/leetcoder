class Solution {
public:
    int maxProduct(int n) {
        int d, d1 = 0, d2 = 0;

        while (n) {
            d = n % 10;
            n /= 10;

            if (d >= d1) {
                d2 = d1;
                d1 = d;
            } else if (d > d2) {
                d2 = d;
            }
        }

        return d1 * d2;
    }
};