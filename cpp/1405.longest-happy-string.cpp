#include <string>
using std::string;

class Solution {
public:
  string longestDiverseString(int a, int b, int c) {
    string res;

    int total = a + b + c;
    int curA = 0, curB = 0, curC = 0;

    for (int i = 0; i < total; i++) {
      if ((a >= b && a >= c && curA < 2) ||
          (a > 0 && (curB >= 2 || curC >= 2))) {
        res.push_back('a');
        a--;
        curA++, curB = 0, curC = 0;
      } else if ((b >= a && b >= c && curB < 2) ||
                 (b > 0 && (curA >= 2 || curC >= 2))) {
        res.push_back('b');
        b--;
        curA = 0, curB++, curC = 0;
      } else if ((c >= a && c >= b && curC < 2) ||
                 (c > 0 && (curA >= 2 || curB >= 2))) {
        res.push_back('c');
        c--;
        curA = 0, curB = 0, curC++;
      } else {
        break;
      }
    }

    return res;
  }
};