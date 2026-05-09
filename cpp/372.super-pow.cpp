class Solution {
private:
    const int mod = 1337;
    int powMod(int base, int exp) {
        base %= mod;
        int result = 1;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = (result * base) % mod;
            }
            exp /= 2;
            base = (base * base) % mod;
        }
        return result;
    }
public:
    int superPow(int a, vector<int>& b) {
        int out = 1;
        for (const int& exp : b) {
            out = powMod(out, 10) * powMod(a, exp);
            out %= mod;
        }
        return out;
    }
};