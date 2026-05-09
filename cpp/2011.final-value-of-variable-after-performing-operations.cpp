#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  int finalValueAfterOperations(vector<string> &operations) {
    int x = 0;

    for (const auto &op : operations) {
      if (op[1] == '+') {
        ++x;
      } else {
        --x;
      }
    }

    return x;
  }
};