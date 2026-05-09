#include <unordered_set>
#include <vector>

using namespace std;

class Solution {

public:
  int distinctPrimeFactors(vector<int> &nums) {
    unordered_set<int> primeFactors;
    unordered_set<int> seen;

    for (int num : nums) {
      if (seen.find(num) != seen.end()) {
        continue;
      }

      seen.insert(num);

      while (num % 2 == 0) {
        num /= 2;
        primeFactors.insert(2);
      }

      for (int j = 3; j * j <= num; j += 2) {
        while (num % j == 0) {
          primeFactors.insert(j);
          num /= j;
        }
      }

      if (num > 1) {
        primeFactors.insert(num);
      }
    }

    return primeFactors.size();
  }
};