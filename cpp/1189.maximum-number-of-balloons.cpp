#include <string>
#include <vector>
using std::vector, std::string;
class Solution {
public:
  int maxNumberOfBalloons(string text) {
    vector<int> count(26, 0);
    for (char c : text) {
      count[c - 'a']++;
    }

    int res = text.size();
    res = std::min(res, count['b' - 'a']);
    res = std::min(res, count['a' - 'a']);
    res = std::min(res, count['l' - 'a'] / 2);
    res = std::min(res, count['o' - 'a'] / 2);
    res = std::min(res, count['n' - 'a']);

    return res;
  }
};