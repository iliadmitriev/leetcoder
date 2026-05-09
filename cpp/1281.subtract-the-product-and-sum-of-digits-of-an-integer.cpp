class Solution {
public:
  int subtractProductAndSum(int n) {
    int p = 1, s = 0;

    for (int i = n; i > 0; i /= 10) {
      p *= i % 10;
      s += i % 10;
    }

    return p - s;
  }
};