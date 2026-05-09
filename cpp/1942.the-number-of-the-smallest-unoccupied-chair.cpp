#include <algorithm>
#include <numeric>
#include <queue>
#include <utility>
#include <vector>

using std::vector, std::priority_queue, std::pair;

class Solution {
public:
  int smallestChair(vector<vector<int>> &times, int targetFriend) {
    int n = times.size();
    vector<int> friends(n);
    std::iota(friends.begin(), friends.end(), 0);

    std::sort(friends.begin(), friends.end(),
              [&](int a, int b) { return times[a][0] < times[b][0]; });

    // occupied chairs by friends (end time, chair num);
    priority_queue<pair<int, int>, vector<pair<int, int>>,
                   std::greater<pair<int, int>>>
        occupiedChairs;

    // free chairs
    priority_queue<int, vector<int>, std::greater<int>> freeChairs;

    int topFreeChair = 0;

    for (int friendId : friends) {
      int start = times[friendId][0];
      int end = times[friendId][1];

      while (occupiedChairs.size() && occupiedChairs.top().first <= start) {
        int free = occupiedChairs.top().second;
        occupiedChairs.pop();

        if (free + 1 == topFreeChair) {
          topFreeChair--;
        } else {
          freeChairs.push(free);
        }
      }

      int chair = -1;
      if (freeChairs.size()) {
        chair = freeChairs.top();
        freeChairs.pop();
      } else {
        chair = topFreeChair++;
      }

      if (friendId == targetFriend) {
        return chair;
      }

      occupiedChairs.push({end, chair});
    }

    return -1;
  }
};