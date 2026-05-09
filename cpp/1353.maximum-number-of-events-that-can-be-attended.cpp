#include <algorithm>
#include <queue>
#include <vector>
using std::vector, std::priority_queue;

class Solution {
public:
  int maxEvents(vector<vector<int>> &events) {
    const int n = events.size();
    int maxEvents = 0, day = 1, i = 0;

    priority_queue<int, vector<int>, std::greater<int>> pq;

    std::sort(events.begin(), events.end());

    while (i < n || pq.size()) {
      // skip days (fast forward) if no event can be attended
      if (pq.empty()) {
        day = events[i][0];
      }

      // add all events that can be possibly attended
      while (i < n && events[i][0] <= day) {
        pq.push(events[i][1]);
        i++;
      }

      // attend the event with the earliest end time
      pq.pop();
      maxEvents++;
      day++;

      // remove all event that impossible to attent
      while (pq.size() && pq.top() < day) {
        pq.pop();
      }
    }

    return maxEvents;
  }
};