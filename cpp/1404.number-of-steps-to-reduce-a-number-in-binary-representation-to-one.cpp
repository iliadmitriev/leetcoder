
class Solution {
public:
  int numSteps(string s) {

    int digit = 0, carry = 0, moves = 0;

    for (int i = s.size() - 1; i > 0; i--) {
      digit = carry + (s[i] - '0');
      moves += 1 + digit % 2;
      carry = (1 + digit) / 2;
    }

    return moves + carry;
  }
};