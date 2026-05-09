
class Solution {
public:
  int minSteps(int n) {
    if (n < 2) {
      return 0;
    }

    int factorSum = 0;

    const int factors[3] = {2, 3, 5};
    // get all factors: 2, 3, 5
    for (int f : factors) {
      while (n % f == 0) {
        factorSum += f;
        n /= f;
      }
    }

    // get increase for:
    // 7, 11, 13, 17, 19, 23, 29, 31
    const int inc[8] = {4, 2, 4, 2, 4, 6, 2, 6};

    int k = 7;

    for (int i = 0; k * k <= n; k += inc[i++ % 8]) {
      while (n % k == 0) {
        factorSum += k;
        n /= k;
      }
    }

    if (n > 1) {
      factorSum += n;
    }

    return factorSum;
  }
};