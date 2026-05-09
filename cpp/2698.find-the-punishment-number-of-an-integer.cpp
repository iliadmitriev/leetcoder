class Solution {
private:
  bool isPunishmentNumber(int num, int target) {
    if (num == 0 && target == 0) {
      return true;
    }

    if (num == 0 || target < 0) {
      return false;
    }

    int place = 1;
    while (num / place > 0) {
      place *= 10;

      if (isPunishmentNumber(num / place, target - num % place)) {
        return true;
      }
    }

    return false;
  }

public:
  int punishmentNumber(int n) {
    int total = 0;

    for (int num = 1; num <= n; num++) {
      int value = num * num;
      if (isPunishmentNumber(value, num)) {
        total += value;
      }
    }

    return total;
  }
};