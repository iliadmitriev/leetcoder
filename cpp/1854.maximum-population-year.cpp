#include <vector>

using std::vector;

class Solution {
public:
  int maximumPopulation(vector<vector<int>> &logs) {

    int maxYear = 0, maxPopulation = 0, curPopulation = 0;

    vector<int> population(101, 0);
    const int shift = 1950;

    for (const auto &log : logs) {
      population[log[0] - shift]++;
      population[log[1] - shift]--;
    }

    for (int i = 0; i < population.size(); i++) {
      curPopulation += population[i];

      if (curPopulation > maxPopulation) {
        maxPopulation = curPopulation;
        maxYear = i;
      }
    }

    return shift + maxYear;
  }
};