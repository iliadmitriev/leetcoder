#include <cmath>
#include <vector>
using std::vector;

class Solution {
public:
  vector<int> constructRectangle(int area) {
    int side = std::sqrt(area);

    while (area % side) {
      side--;
    }

    return {area / side, side};
  }
};