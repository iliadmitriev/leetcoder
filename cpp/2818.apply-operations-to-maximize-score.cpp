#include <numeric>
#include <unordered_map>
#include <vector>
using std::vector, std::unordered_map;

class Solution {
private:
  int getPrimeScore(unordered_map<int, int> &cache, int num) {
    int key = num;
    if (cache.find(key) != cache.end()) {
      return cache[key];
    }

    int score = 0;

    if (num % 2 == 0) {
      score++;
    }

    while (num % 2 == 0) {
      num /= 2;
    }

    for (int i = 3; i * i <= num; i += 2) {
      if (num % i == 0) {
        score++;
      }
      while (num % i == 0) {
        num /= i;
      }
    }

    if (num > 2) {
      score++;
    }

    return cache[key] = score;
  }

  int exponent(long base, int exp, int mod) {
    long res = 1;

    base %= mod;

    while (exp) {
      if (exp & 1) {
        res *= base;
        res %= mod;
      }
      base *= base;
      base %= mod;
      exp >>= 1;
    }
    return res;
  }

public:
  int maximumScore(vector<int> &nums, int k) {
    const int n = nums.size();
    const int MOD = int(1e9) + 7;

    unordered_map<int, int> cache;
    vector<int> scores(n);
    vector<int> left(n, -1), right(n, n);
    vector<int> stack, idx(n);
    long res = 1;

    std::transform(nums.begin(), nums.end(), scores.begin(),
                   [&](int num) { return this->getPrimeScore(cache, num); });
    std::iota(idx.begin(), idx.end(), 0);

    std::sort(idx.begin(), idx.end(), [&nums](int i, int j) {
      if (nums[i] == nums[j])
        return i < j;
      return nums[i] < nums[j];
    });

    // build left bounds array for every number
    stack.clear();
    for (int i = 0; i < n; i++) {
      while (stack.size() && scores[stack.back()] < scores[i]) {
        stack.pop_back();
      }
      left[i] = stack.size() ? stack.back() : -1;
      stack.push_back(i);
    }

    // build right bounds array for every number
    stack.clear();
    for (int i = n - 1; i >= 0; i--) {
      while (stack.size() && scores[stack.back()] <= scores[i]) {
        stack.pop_back();
      }
      right[i] = stack.size() ? stack.back() : n;
      stack.push_back(i);
    }

    while (idx.size() && k > 0) {
      int i = idx.back();
      idx.pop_back();

      int num = nums[i];
      int l = i - left[i], r = right[i] - i;

      int step = std::min(long(k), long(l) * r);

      res *= exponent(num, step, MOD);
      res %= MOD;
      k -= step;
    }

    return res;
  }
};
