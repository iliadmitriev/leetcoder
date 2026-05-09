#include <cmath>
#include <vector>
using std::vector;

class Solution {
public:
  vector<int> distributeCandies(int candies, int num_people) {
    vector<int> res(num_people, 0);

    int n = (std::sqrt(8L * candies + 1) - 1) / 2;
    int s = n * (n + 1) / 2;

    for (int i = 0; i < num_people; i++) {
      int n_cur = n / num_people + (i < n % num_people ? 1 : 0);
      int s_cur = n_cur * (2 * (i + 1) + (n_cur - 1) * num_people) / 2;

      res[i] = s_cur;
    }

    int leftover = candies - s;
    res[n % num_people] += leftover;

    return res;
  }
};