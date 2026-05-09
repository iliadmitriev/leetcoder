#include <vector>
using std::vector;

class Solution {
public:
  int numOfUnplacedFruits(vector<int> &fruits, vector<int> &baskets) {
    const int n = baskets.size();
    int left = n;

    for (int fruit : fruits) {
      for (int j = 0; j < n; j++) {
        if (fruit <= baskets[j]) {
          baskets[j] = -1;
          left--;
          break;
        }
      }
    }

    return left;
  }
};