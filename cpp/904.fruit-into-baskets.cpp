#include <unordered_map>
#include <vector>
using std::vector, std::unordered_map;

class Solution {
public:
  int totalFruit(vector<int> &fruits) {
    const int n = fruits.size();
    int maxFruits = 0;
    unordered_map<int, int> cnt;

    for (int i = 0, j = 0; i < n; i++) {
      cnt[fruits[i]]++;

      while (cnt.size() > 2) {
        cnt[fruits[j]]--;

        if (cnt[fruits[j]] == 0) {
          cnt.erase(fruits[j]);
        }

        j++;
      }

      maxFruits = std::max(maxFruits, i - j + 1);
    }

    return maxFruits;
  }
};