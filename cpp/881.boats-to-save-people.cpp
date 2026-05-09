#include <vector>

using namespace std;

class Solution {
public:
  int numRescueBoats(vector<int> &people, int limit) {
    int boats = 0;

    int max_weight = *max_element(people.begin(), people.end());
    vector<int> weight(max_weight + 1, 0);
    for (auto person : people) {
      weight[person]++;
    }

    int left = 0, right = max_weight;

    while (left <= right) {
      while (left <= right && weight[left] <= 0)
        left++;

      while (left <= right && weight[right] <= 0)
        right--;

      if (left > right)
        break;

      if (left + right <= limit) {
        weight[left]--;
      }

      weight[right]--;

      boats++;
    }

    return boats;
  }
};