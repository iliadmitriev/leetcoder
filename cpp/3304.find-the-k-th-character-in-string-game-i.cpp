class Solution {
public:
  char kthCharacter(int k) {
    int n = 0;

    k--;

    while (k) {
      n++;
      k &= k - 1;
    }

    return 'a' + n;
  }
};