#include <vector>
using std::vector;

class Solution {
public:
    vector<int> evenOddBit(int n) {
      vector<int> res(2, 0);
      int i = 0;

      while (n) {
        res[i] += n & 1; 
        i ^= 1;
        n >>= 1;
      }

      return res;
    }
};