#include <string>
using std::string;

class Solution {
public:
  bool isCircularSentence(string sentence) {

    if (sentence.front() != sentence.back()) {
      return false;
    }
    int i = 0, n = sentence.size();

    while (i < n) {
      if (sentence[i] != ' ') {
        i++;
        continue;
      }

      // if (i == n - 1 || i == 0) {
      //   return false;
      // }

      if (sentence[i - 1] != sentence[i + 1]) {
        return false;
      }
      i++;
    }

    return i == n;
  }
};