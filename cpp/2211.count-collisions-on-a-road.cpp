#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
  int countCollisions(string directions) {
    const int n = directions.size();
    int collisions = 0;
    vector<int> stack;
    stack.reserve(n);

    auto to_int = [](char c) -> int {
      switch (c) {
      case 'L':
        return -1;
      case 'R':
        return 1;
      }
      return 0;
    };

    for (char d : directions) {
      int dd = to_int(d);

      while (!stack.empty() && stack.back() > dd) {
        collisions += stack.back() - dd;
        stack.pop_back();
        dd = 0;
      }

      stack.push_back(dd);
    }

    return collisions;
  }
};