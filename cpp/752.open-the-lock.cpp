#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int openLock(vector<string> &deadends, string target) {
    queue<pair<string, int>> q;
    set<string> dead(deadends.begin(), deadends.end());

    if (dead.find("0000") != dead.end() || dead.find(target) != dead.end()) {
      return -1;
    }

    q.push({"0000", 0});
    dead.insert("0000");

    while (!q.empty()) {
      auto [s, cnt] = q.front();
      q.pop();

      if (s == target) {
        return cnt;
      }

      for (int i = 0; i < 4; ++i) {
        for (int d : {1, -1}) {
          string t = s;
          t[i] = (t[i] - '0' + d + 10) % 10 + '0';

          if (dead.find(t) == dead.end()) {
            q.push({t, cnt + 1});
            dead.insert(t);
          }
        }
      }
    }

    return -1;
  }
};