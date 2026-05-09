class Solution {
public:
  int pivotInteger(int n) {

    int prefix = 0, suffix = n * (n + 1) / 2;

    for (int i = 1; i <= n; i++) {
      prefix += i;

      if (prefix == suffix) {

        return i;
      }

      suffix -= i;
    }

    return -1;
  }
};