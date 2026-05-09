#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  int minOperations(vector<string> &logs) {
    int path = 0;

    for (const string &log : logs) {
      if (log == "../") {
        if (path) {
          path--;
        }
      } else if (log != "./") {
        path++;
      }
    }

    return path;
  }
};