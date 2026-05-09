#include <queue>
#include <vector>

using std::vector, std::queue;
class Solution {
public:
  int maxCandies(vector<int> &status, vector<int> &candies,
                 vector<vector<int>> &keys, vector<vector<int>> &containedBoxes,
                 vector<int> &initialBoxes) {
    int total = 0;
    queue<int> q;

    // statuses
    // 0: locked
    // 1: unlocked
    // -1: visited, locked
    // -2: visited, unloked

    for (int box : initialBoxes) {
      if (status[box] == 1) {
        q.push(box);
        status[box] = -2;
      } else if (status[box] == 0) {
        status[box] = -1;
      }
    }

    while (q.size()) {
      int box = q.front();
      total += candies[box];

      for (int key : keys[box]) {
        if (status[key] == -1) { // visited before but locked
          q.push(key);           // visit again
        }
        status[key] = 1; // unlock
      }

      for (int nextBox : containedBoxes[box]) {
        if (status[nextBox] == 1) {
          q.push(nextBox);
          status[nextBox] = -2;
        } else if (status[nextBox] == 0) {
          status[nextBox] = -1;
        }
      }

      q.pop();
    }

    return total;
  }
};