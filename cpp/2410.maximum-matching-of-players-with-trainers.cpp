#include <vector>
using std::vector;

class Solution {
public:
  int matchPlayersAndTrainers(vector<int> &players, vector<int> &trainers) {
    const int m = players.size(), n = trainers.size();
    int count = 0;

    std::sort(players.begin(), players.end());
    std::sort(trainers.begin(), trainers.end());

    for (int i = 0, j = 0; i < m && j < n; j++) {
      if (players[i] <= trainers[j]) {
        count++;
        i++;
      }
    }

    return count;
  }
};