#include <string>
#include <unordered_map>
#include <vector>

using std::string;
using std::unordered_map;
using std::vector;
template <typename T> T modpow(T base, T exp, T mod) {
  base %= mod;
  T result = 1;

  while (exp > 0) {
    if (exp & 1)
      result = (result * base) % mod;
    base = (base * base) % mod;
    exp >>= 1;
    // result = (base * result) % mod;
    // exp--;
  }

  return result;
}

class Solution {
private:
  string robinKarp(string &s, int maxLen) {

    if (maxLen == 0) {
      return "";
    }

    const long mod = 1000000007;
    const int base = 31;
    const long upperBase = modpow<long>(base, maxLen - 1, mod);
    const int shift = 'A' - 1;

    long prefix = 0;

    for (int i = 0; i < maxLen; i++) {
      prefix = (prefix * base + s[i] - shift) % mod;
    }

    unordered_map<long, vector<int>> seen;
    seen[prefix].push_back(0);

    for (int i = maxLen; i < s.size(); i++) {
      // add mod * base to avoid negative values
      // remove most significant value from prefix hash using upperBase
      prefix = (mod * base + prefix - upperBase * (s[i - maxLen] - shift)) % mod;
      prefix = (prefix * base + s[i] - shift) % mod;

        // fix negative values
        while(prefix<0) {
            prefix += mod;
        }
        prefix %= mod;


      if (seen.count(prefix)) {
        for (int idx : seen[prefix]) {
          if (s.substr(i - maxLen + 1, maxLen) == s.substr(idx, maxLen))
            return s.substr(idx, maxLen);
        }
      }

      seen[prefix].push_back(i - maxLen + 1);
    }

    return "";
  }

public:
  string longestDupSubstring(string s) {
    int lo = 1, hi = s.size();
    int mid;
    string res;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      string ret = robinKarp(s, mid);
      if (ret.size() > 0) {
        res = ret;
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }

    return res;
  }
};
