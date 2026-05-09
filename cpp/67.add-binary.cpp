class Solution {
public:
    string addBinary(string a, string b) {
        const int m = a.size(), n = b.size();
        const int p = std::max(m, n) + 1;
        const char base = '0';

        int i = m, j = n, k = p;
        char carry = 0;
        std::string c(p, 0);

        while (i || j || carry) {

            if (i) {
                carry += a[--i] ^ base;
            }

            if (j) {
                carry += b[--j] ^ base;
            }

            c[--k] = (carry & 1) ^ base;
            carry >>= 1;
        }

        if (k) {
            return c.substr(k);
        }

        return c;
    }
};