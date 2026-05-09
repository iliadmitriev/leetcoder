
class Solution {
public:
  int differenceOfSums(int n, int m) {
    int num1 = (n * (n + 1)) / 2, k = n / m;
    int num2 = (k * (k + 1)) / 2 * m;

    return num1 - 2 * num2;
  }
};