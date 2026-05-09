class Solution {
public:
    double myPow(double x, long n) {
        if (n == 0) {
            return 1.0;
        } else if (n < 0) {
            return 1 / myPow(x, -n);
        } else if (n % 2) {
            return x * myPow(x * x, n / 2);
        } else {
            return myPow(x * x, n / 2);
        }
    }
};