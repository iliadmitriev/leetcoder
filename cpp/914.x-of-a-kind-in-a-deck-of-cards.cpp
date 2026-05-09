#include <numeric>
#include <unordered_map>
#include <vector>
using std::unordered_map;
using std::vector;

class Solution {
public:
  bool hasGroupsSizeX(vector<int> &deck) {
    unordered_map<int, int> freq;

    for (int card : deck) {
      freq[card]++;
    }

    vector<int> fr;
    fr.reserve(freq.size());
    for (auto [_, f] : freq) {
      fr.push_back(f);
    }

    int divisor = std::reduce(fr.begin(), fr.end(), fr.front(),
                              [&](int a, int b) { return std::gcd(a, b); });

    return divisor >= 2;
  }
};