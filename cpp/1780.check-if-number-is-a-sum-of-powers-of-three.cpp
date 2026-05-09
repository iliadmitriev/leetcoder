class Solution {
public:
  bool checkPowersOfThree(int n) {
    int r;
    while (n) {
      r = n % 3;
      n /= 3;

      if (r == 2) {
        return false;
      }
    }

    return true;
  }
};