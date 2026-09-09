class Solution {
public:
    long long countCommas(long long n) {
        long long res = 0;
        long long exp = 1000; // exponent: 1e3, 1e6, 1e9, 1e12, ...
        long long nexp = exp * 1000; // next exponent
        long long p = 1; // power: 1, 2, 3, 4, ...

        while (exp <= n) {
          nexp = std::min(n + 1L, exp * 1000L); // nexp is the next exponent (or n inclusive)
          
          res += (nexp - exp) * p;

          exp = nexp;
          p += 1;
        }

        return res;
    }
};