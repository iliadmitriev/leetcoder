#include <algorithm>
#include <cstdlib>
#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
public:
  long long minCost(vector<int> &basket1, vector<int> &basket2) {
    unordered_map<int, int> freq;
    int minFruit = basket1.front();
    vector<int> merged;

    // balance the fruits
    for (int fruit : basket1) {
      freq[fruit]++;
      minFruit = std::min(minFruit, fruit);
    }

    // balance the fruits
    for (int fruit : basket2) {
      freq[fruit]--;
      minFruit = std::min(minFruit, fruit);
    }

    for (auto [fruit, count] : freq) {
      if (count % 2 != 0) {
        return -1;
      }

      int imbalanced = std::abs(count) / 2;

      for (int i = 0; i < imbalanced; i++) {
        merged.push_back(fruit);
      }
    }

    if (merged.empty()) {
      return 0;
    }

    std::sort(merged.begin(), merged.end());

    long long cost = 0;
    for (int i = 0; i < merged.size() / 2; i++) {
      cost += std::min(minFruit * 2, merged[i]);
    }

    return cost;
  }
};