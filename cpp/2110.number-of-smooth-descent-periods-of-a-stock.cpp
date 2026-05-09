#include <vector>
using std::vector;

class Solution {
public:
  long long getDescentPeriods(vector<int> &prices) {
    typedef long long ll;

    ll total = 0;
    int window = 1, prev = -1;

    for (int price : prices) {
      if (prev - 1 == price) {
        window++;
      } else {
        window = 1;
      }

      total += window;
      prev = price;
    }

    return total;
  }
};