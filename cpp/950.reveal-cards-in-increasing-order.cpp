#include <algorithm>
#include <deque>
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> deckRevealedIncreasing(vector<int> &deck) {
    int n = deck.size();

    vector<int> res(n);
    deque<int> q;

    for (int i = 0; i < n; i++) {
      q.push_back(i);
    }

    sort(deck.begin(), deck.end());

    for (auto d : deck) {
      res[q.front()] = d;
      q.pop_front();

      if (!q.empty()) {
        q.push_back(q.front());
        q.pop_front();
      }
    }

    return res;
  }
};