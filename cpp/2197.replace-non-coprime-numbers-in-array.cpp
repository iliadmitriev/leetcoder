#include <vector>
using std::vector;

class Solution {
private:
  inline int gcd(int a, int b) {
    while (b) {
      // a, b = b, a % b
      a %= b;
      std::swap(a, b);
    }

    return a;
  }

  inline int coprime(int a, int b) { return gcd(a, b) == 1; }

  inline int lcm(int a, int b) { return a / gcd(a, b) * b; }

public:
  vector<int> replaceNonCoprimes(vector<int> &nums) {
    const int n = nums.size();
    vector<int> res;
    res.reserve(n);

    int cur = nums.front();
    res.push_back(cur);

    for (int i = 1; i < n; i++) {
      if (!coprime(cur, nums[i])) {
        cur = lcm(cur, nums[i]);

        while (!res.empty() && !(coprime(cur, res.back()))) {
          cur = lcm(cur, res.back());
          res.pop_back();
        }

        res.push_back(cur);

      } else {
        cur = nums[i];
        res.push_back(cur);
      }
    }

    return res;
  }
};