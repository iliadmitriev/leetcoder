#include <vector>

using namespace std;

class Solution {
public:
  int timeRequiredToBuy(vector<int> &tickets, int k) {
    int t = 0;
    int top = tickets[k];

    for (int i = 0; i < tickets.size(); ++i) {
      if (i <= k) {
        t += min(top, tickets[i]);
      } else {
        t += min(top - 1, tickets[i]);
      }
    }

    return t;
  }
};