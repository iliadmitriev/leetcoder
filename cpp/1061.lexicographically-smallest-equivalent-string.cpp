#include <array>
#include <numeric>
#include <string>

using std::string, std::array;

class UF {
private:
  array<char, 26> par;

public:
  UF() { std::iota(par.begin(), par.end(), 0); }

  char find(char x) {
    while (x != par[x]) {
      par[x] = par[par[x]];
      x = par[x];
    }
    return x;
  }

  void join(char x, char y) {
    x = find(x);
    y = find(y);
    if (x == y) {
      return;
    }

    if (x < y) {
      par[y] = x;
    } else {
      par[x] = y;
    }
  }

  char findBased(char x) { return find(x - 'a') + 'a'; }
  void joinBased(char x, char y) { join(x - 'a', y - 'a'); }
};

class Solution {
public:
  string smallestEquivalentString(string s1, string s2, string baseStr) {
    UF uf;
    const int n = s1.size();
    for (int i = 0; i < n; i++) {
      uf.joinBased(s1[i], s2[i]);
    }

    string res;
    res.reserve(baseStr.size());

    for (char c : baseStr) {
      res += uf.findBased(c);
    }
    return res;
  }
};