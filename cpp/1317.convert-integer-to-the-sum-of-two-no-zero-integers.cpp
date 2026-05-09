#include <vector>
using std::vector;

class Solution {
public:
  vector<int> getNoZeroIntegers(int n) {
    int a = 0, b = 0;
    int p = 1; // decimal place (power of 10)
    int d = 0; // current digit of number n (0-9) from rightmost to leftmost
               // place of n

    while (n) {
      d = n % 10;
      n /= 10;

      // if current digit is >= 2 or this is a rightmost digit (there is no
      // carry available)
      if (d >= 2 || n == 0) {
        a += p * (1);
        b += p * (d - 1);
      } else {
        a += p * (9);
        b += p * (d + 1); // 1 or 2
        n--;
      }

      p *= 10;
    }

    return {a, b};
  }
};