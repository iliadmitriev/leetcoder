#include <map>
#include <queue>
#include <vector>

using std::map;
using std::priority_queue;
using std::vector;

class Solution {
public:
  bool isNStraightHand(vector<int> &hand, int groupSize) {
    if (hand.size() % groupSize != 0)
      return false;

    map<int, int> counter;
    for (auto card : hand) {
      counter[card]++;
    }

    priority_queue<int, vector<int>, std::greater<int>> pq;
    for (auto [card, _] : counter) {
      pq.push(card);
    }

    while (!pq.empty()) {
      int minNum = pq.top();

      for (int card = minNum; card < minNum + groupSize; card++) {
        if (counter[card] == 0)
          return false;

        counter[card]--;

        if (counter[card] == 0) {
          if (card != pq.top())
            return false;

          pq.pop();
        }
      }
    }

    return true;
  }
};