class Solution {
private:
    // calculate number of combinations (n choose k)
    int combinations(int n, int k) {
        if (k == 0) return 1;

        if (k > n / 2) return combinations(n, n - k);

        long res = 1;

        for (int r = 1; r <= k; ++r) {
            res *= n - r + 1;
            res /= r;
        }
        return res;
    }

public:
    int uniquePaths(int m, int n) {        
        return combinations(m + n - 2, n - 1);
    }
};