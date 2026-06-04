class Solution {
public:
    int totalWaviness(int num1, int num2) {
        auto count = [](int x) -> int {
          if (x < 100) {
            return 0;
          }
          
          int c = 0, r;

          int r2 = x % 10;
          x /= 10;
          int r1 = x % 10;
          x /= 10;

          while (x) {
            r = x % 10;
            x /= 10;

            c += (r2 < r1 && r1 > r) || (r2 > r1 && r1 < r);

            r2 = r1;
            r1 = r;
          }

          return c;
        };

        int res = 0;
        for (int x = num1; x <= num2; x++) {
          res += count(x);
        }

        return res;
    }
};