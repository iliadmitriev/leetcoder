class Solution {
public:
    int countCommas(int n) {
        int e = 1000; // exponent
        int p = 1; // power
        int res = 0;

        while (e <= n) {
          int ne = std::min(n + 1, e * 1000);
          
          res += (ne - e) * p;

          e = ne;
          p++;
        }

        return res;
    }
};