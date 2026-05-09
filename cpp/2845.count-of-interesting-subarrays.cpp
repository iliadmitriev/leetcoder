#include <unordered_map>
#include <vector>
using std::vector, std::unordered_map;

class Solution {
public:
  long long countInterestingSubarrays(vector<int> &nums, int modulo, int k) {
    long long total = 0L;
    int prefix = 0;
    unordered_map<int, int> cache;

    cache[0] = 1;

    for (int num : nums) {
      prefix += int(num % modulo == k);
      auto left = (prefix - k + modulo) % modulo;
      total += cache[left];
      cache[prefix % modulo]++;
    }

    return total;
  }
};