#include <algorithm>
#include <numeric>
#include <vector>
using std::vector;

class Solution {
public:
  int distanceBetweenBusStops(vector<int> &distance, int start,
                              int destination) {
    int total = std::accumulate(distance.begin(), distance.end(), 0);

    if (start > destination) {
      std::swap(start, destination);
    }

    int diff = std::accumulate(distance.begin() + start,
                               distance.begin() + destination, 0);

    return std::min(total - diff, diff);
  }
};