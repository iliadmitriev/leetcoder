#include <unordered_map>
#include <vector>
using std::vector, std::unordered_map;

class Solution {
public:
  int numRabbits(vector<int> &answers) {
    int total = 0;
    unordered_map<int, int> m;
    for (int answer : answers) {
      m[answer]++;
    }

    // ceil function replaced with integer division
    // ceil(a / b) =  (a + b - 1) / (b)
    for (auto [k, v] : m) {
      total += (k + v) / (k + 1) * (k + 1);
    }
    return total;
  }
};