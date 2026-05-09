#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
  int countStudents(vector<int> &students, vector<int> &sandwiches) {
    vector<int> cnt(2, 0);

    for (int student : students) {
      cnt[student]++;
    }

    for (int sandwich : sandwiches) {
      if (cnt[sandwich] > 0) {
        cnt[sandwich]--;
      } else {
        break;
      }
    }

    return cnt[0] + cnt[1];
  }
};