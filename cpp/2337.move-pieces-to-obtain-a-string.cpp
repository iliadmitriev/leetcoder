#include <string>
using std::string;

class Solution {
public:
  bool canChange(string start, string target) {
    const int m = start.size();

    // R: start, target
    // L: target, start
    int left = 0, right = 0;

    for (int i = 0; i < m; i++) {
      // open R
      if (start[i] == 'R') {
        if (left > 0) {
          return false;
        }
        right++;
      }
      // open L
      if (target[i] == 'L') {
        if (right > 0) {
          return false;
        }
        left++;
      }
      // close R
      if (target[i] == 'R') {
        if (right == 0) {
          return false;
        }
        right--;
      }
      // close L
      if (start[i] == 'L') {
        if (left == 0) {
          return false;
        }
        left--;
      }
    }

    return left == 0 && right == 0;
  }
};