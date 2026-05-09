class Solution {
private:
    int isSquare(int n) {
        int q = int(std::sqrt(float(n)));
        return q * q == n;
    }
public:
    int numSquares(int n) {
        while ((n & 3) == 0) {
            n >>= 2;
        }

        if ((n & 7) == 7) {
            return 4;
        }

        if (isSquare(n)) {
            return 1;
        }

        int q = int(std::sqrt(float(n)));
        for (int i = 1; i <= q; i++) {
            if (isSquare(n - i * i)) {
                return 2;
            }
        }

        return 3;
    }
};