#include <cmath>
class Solution {
private:
  // Sqrt using Newton's method
  double sqrt(double x) {
    double y = x;

    while (std::abs(y * y - x) > 1e-6) {
      y = (y + (x / y)) / 2;
    }
    return y;
  }

public:
  bool isPerfectSquare(int num) {
    int x = sqrt(num);

    return x * x == num;
  }
};