class Solution {
public:
  int tribonacci(int n) {
    if (n == 0)
      return 0;
    if (n == 1 || n == 2)
      return 1;

    int res = 0, t1 = 0, t2 = 1, t3 = 1;

    for (int i = 2; i < n; ++i) {
      res = t1 + t2 + t3;
      t1 = t2;
      t2 = t3;
      t3 = res;
    }

    return res;
  }
};