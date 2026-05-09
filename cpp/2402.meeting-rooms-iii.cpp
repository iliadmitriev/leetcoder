#include <queue>
#include <utility>
#include <vector>

using std::vector, std::priority_queue, std::pair, std::greater;

class Solution {
public:
  int mostBooked(int n, vector<vector<int>> &meetings) {
    vector<int> res(n, 0);

    sort(meetings.begin(), meetings.end(),
         [](const auto &p1, const auto &p2) -> bool {
           return p1[0] == p2[0] ? p1[1] < p2[1] : p1[0] < p2[0];
         });

    priority_queue<int, vector<int>, greater<int>> free;
    for (int i = 0; i < n; i++) {
      free.push(i);
    }

    priority_queue<pair<long, int>, vector<pair<long, int>>,
                   greater<pair<long, int>>>
        busy;

    for (const auto &meeting : meetings) {
      int start = meeting[0];
      int end = meeting[1];

      while (!busy.empty() && busy.top().first <= start) {
        free.push(busy.top().second);
        busy.pop();
      }

      if (!free.empty()) { // there is free meeting rooms
        int room = free.top();
        free.pop();
        busy.push({end, room});
        res[room]++;
      } else { // there is no free meeting rooms, postpone meeting
        int room = busy.top().second;
        long diff = busy.top().first - start;
        busy.pop();
        busy.push({diff + end, room});
        res[room]++;
      }
    }

    int max_meetins = 0;
    for (int i = 0; i < n; i++) {
      if (res[i] > res[max_meetins]) {
        max_meetins = i;
      }
    }

    return max_meetins;
  }
};