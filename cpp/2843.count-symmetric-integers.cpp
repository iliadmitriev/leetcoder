
class Solution {
private:
  int dsum(int num) {
    int res = 0;
    while (num) {
      res += num % 10;
      num /= 10;
    }
    return res;
  }

  bool symmetric(int num) {
    int size = 0, div = 0;
    if (10 <= num && num < 100) {
      size = 2;
      div = 10;
    } else if (1'000 <= num && num < 10'000) {
      size = 4;
      div = 100;
    } else {
      return false;
    }

    if (size % 2 != 0) {
      return false;
    }

    int left = num / div;
    int right = num % div;

    return dsum(left) == dsum(right);
  }

public:
  int countSymmetricIntegers(int low, int high) {

    int res = 0;
    for (int i = low; i <= high; i++) {
      if (symmetric(i)) {
        res++;
      }
    }
    return res;
  }
};