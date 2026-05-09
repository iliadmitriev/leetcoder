#include <unordered_set>
class Solution {
public:
  bool isHappy(int n) {

    std::unordered_set<int> s;
    s.insert(n);

    int n2, x;
    while (n != 1) {
      n2 = 0;

      while (n) {
        x = n % 10;
        n /= 10;

        n2 += x * x;
      }

      n = n2;
      if (s.find(n) != s.end()) {
        return false;
      }

      s.insert(n);
    }

    return true;
  }
};
