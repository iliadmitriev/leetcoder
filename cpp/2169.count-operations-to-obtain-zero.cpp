
class Solution {
public:
  int countOperations(int num1, int num2) {
    int i = 0, tmp;

    while (num2) {
      i += num1 / num2;

      tmp = num1 % num2;
      num1 = num2;
      num2 = tmp;
    }

    return i;
  }
};