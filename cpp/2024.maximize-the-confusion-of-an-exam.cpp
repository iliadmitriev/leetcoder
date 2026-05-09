#include <string>

using std::max;
using std::string;

class Solution {
public:
  int maxConsecutiveAnswers(string answerKey, int k) {
    int lT = 0, kT = k, lF = 0, kF = k;
    int maxConsecutive = 0;

    for (int r = 0; r < answerKey.length(); r++) {
      kT -= answerKey[r] == 'F';
      kF -= answerKey[r] == 'T';

      if (kT < 0) {
        kT += answerKey[lT++] == 'F';
      }

      if (kF < 0) {
        kF += answerKey[lF++] == 'T';
      }

      maxConsecutive = max(maxConsecutive, max(r - lT, r - lF) + 1);
    }

    return maxConsecutive;
  }
};