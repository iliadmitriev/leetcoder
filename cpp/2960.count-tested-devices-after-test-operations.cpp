#include <vector>

using std::vector;

class Solution {
public:
  int countTestedDevices(vector<int> &batteryPercentages) {
    int devices = 0, discharge = 0;

    for (int charge : batteryPercentages) {
      if (charge > discharge) {
        ++devices;
        ++discharge;
      }
    }

    return devices;
  }
};