#include <numeric>
#include <vector>
using std::vector;

class Solution {
private:
  int encrypt(int num) {
    int counter = 0, maxDigit = 0;

    while (num) {
      maxDigit = std::max(maxDigit, num % 10);
      num /= 10;
      counter++;
    }

    while (counter--) {
      num = num * 10 + maxDigit;
    }

    return num;
  }

public:
  int sumOfEncryptedInt(vector<int> &nums) {
    return std::accumulate(nums.begin(), nums.end(), 0, [&](int acc, int num) {
      return acc + encrypt(num);
    });
  }
};