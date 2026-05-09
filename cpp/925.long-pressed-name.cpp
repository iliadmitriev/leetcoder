#include <string>
using std::string;

class Solution {
public:
  bool isLongPressedName(string name, string typed) {
    const int n = name.size(), t = typed.size();
    int i = 0, j = 0;

    while (i < n && j < t) {
      char a = name[i], b = typed[j];

      if (a != b) {
        return false;
      }

      int c1 = 0, c2 = 0;
      while (i < n && a == name[i]) {
        i++;
        c1++;
      }

      while (j < t && b == typed[j]) {
        j++;
        c2++;
      }

      if (c1 > c2) {
        return false;
      }
    }

    return i == n && j == t;
  }
};