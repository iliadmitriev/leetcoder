#include <string>

using std::string;

class Solution {
private:
  string backtrack(char prev, string &cur, int n, int k, int &count) {
    if (n == cur.size()) {
      count++;

      if (count == k) {
        return cur;
      }

      return "";
    }

    for (char c = 'a'; c <= 'c'; c++) {
      if (c == prev) {
        continue;
      }

      cur.push_back(c);
      string res = backtrack(c, cur, n, k, count);
      cur.pop_back();

      if (res.size() > 0) {
        return res;
      }
    }

    return "";
  }

public:
  string getHappyString(int n, int k) {
    int counter = 0;
    string cur;
    cur.reserve(n);

    return backtrack('x', cur, n, k, counter);
  }
};