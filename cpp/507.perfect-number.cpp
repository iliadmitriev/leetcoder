
class Solution {
public:
  bool checkPerfectNumber(int num) {
    if (num == 1) {
      return false;
    }

    int sum = 1; // total sum of all positive divisors

    for (int i = 2; i * i <= num; i += 2) {
      if (num % i == 0) {
        sum += i;
        sum += num / i;
      }
    }

    return sum == num;
  }
};