#include <algorithm>
#include <string>

using std::string;

class Solution {
public:
  int bestClosingTime(string customers) {
    int n = customers.size();

    int totalPenalty = std::count(customers.begin(), customers.end(), 'Y');
    int minPenalty = totalPenalty;
    int curPenalty = totalPenalty;
    int earliestHour = 0;

    for (int i = 0; i < n; i++) {
      if (customers[i] == 'N') {
        curPenalty++;
      } else {
        curPenalty--;
      }

      if (curPenalty < minPenalty) {
        minPenalty = curPenalty;
        earliestHour = i + 1;
      }
    }

    return earliestHour;
  }
};