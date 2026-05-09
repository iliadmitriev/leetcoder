#include <sstream>
#include <string>
#include <vector>

using std::string, std::vector;
class Solution {
public:
  vector<string> findOcurrences(string text, string first, string second) {
    vector<string> res;
    std::istringstream iss(text);

    string w1, w2, cur;
    const int n = text.size();

    while (iss >> cur) {

      if (w2 == first && w1 == second) {
        res.push_back(cur);
      }

      w2 = w1;
      w1 = cur;
    }

    return res;
  }
};