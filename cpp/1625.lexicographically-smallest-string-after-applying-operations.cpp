#include <string>

using std::string;

static const char BASE = '0';

// gcd - calculates the greatest common divisor for a and b
int gcd(int a, int b) {
  while (b) {
    a %= b;
    std::swap(a, b);
  }
  return a;
}

class Solution {
public:
  string findLexSmallestString(string s, int a, int b) {
    const int n = s.size();       // length of digits chain
    const int rot = gcd(b, n);    // rotation step for digits chain
    const int shift = gcd(a, 10); // rotation step for a single digit

    string res = s;

    // rotate digits chain
    // i - parity of digits chain (0, 1)
    auto rotate = [shift](string &t, int i) -> void {
      const int n = t.size();
      int c = t[i] - BASE; // first digit, to make it as small as possible
      // calculate minimal possible value for the first digit (mod bu group
      // size)
      int inc = (10 + c % shift - c) % 10;

      if (!inc) {
        return;
      }

      for (int j = i; j < n; j += 2) {
        t[j] = ((t[j] - BASE) + inc) % 10 + BASE;
      }
    };

    // try all possible rotations of digits chain
    for (int i = 0; i < n; i += rot) {
      string t =
          string(s.begin() + i, s.end()) + string(s.begin(), s.begin() + i);
      rotate(t, 1);

      if (rot % 2 == 1) {
        rotate(t, 0);
      }

      res = std::min(res, t);
    }

    return res;
  }
};