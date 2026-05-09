class Solution {
public:
    int countOrders(int n) {
        int mod = 1E9 + 7;

        long res = 1;

        for (int i = 1; i <= n; i++) {
            int valid_choises = i * (2 * i - 1);
            res *= valid_choises;
            res %= mod;
        }

        return res;
    }
};