#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
  string removeKdigits(string num, int k) {
    string res;

    for (char c : num) {
      while (k && res.size() && res.back() > c) {
        res.pop_back();
        k--;
      }

      if (res.size() || c != '0')
        res.push_back(c);
    }

    if (k) {
      res.erase(max(0, int(res.size() - k)), k);
    }

    return res.size() ? res : "0";
  }
};