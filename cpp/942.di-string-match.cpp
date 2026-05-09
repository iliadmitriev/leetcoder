#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  vector<int> diStringMatch(string s) {
    vector<int> result;
    int lo = 0, hi = s.size();

    for (char ch : s) {
      if (ch == 'D') {
        result.push_back(hi--);
      } else {
        result.push_back(lo++);
      }
    }

    result.push_back(lo); // or hi
    return result;
  }
};