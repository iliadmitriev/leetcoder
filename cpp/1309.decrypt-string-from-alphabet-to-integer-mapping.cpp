#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
  string freqAlphabets(string s) {
    vector<int> tmp;

    for (char ch : s) {
      if (ch == '#') {
        char a = tmp.back();
        tmp.pop_back();
        char b = tmp.back();
        tmp.pop_back();

        tmp.push_back(10 * b + a);
      } else {
        tmp.push_back(ch - '0');
      }
    }

    const int base = 'a' - 1;
    string res;

    for (int i = 0; i < tmp.size(); i++) {
      res.push_back(base + tmp[i]);
    }

    return res;
  }
};