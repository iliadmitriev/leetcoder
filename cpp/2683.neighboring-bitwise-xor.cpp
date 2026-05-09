#include <vector>
using std::vector;

class Solution {
public:
  bool doesValidArrayExist(vector<int> &derived) {
    int cur = 0;
    for (auto v : derived) {
      cur ^= v;
    }
    return cur == 0;
  }
};