#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;

class Solution {
public:
  bool lemonadeChange(vector<int> &bills) {
    unordered_map<int, int> collected;
    const int price = 5;

    for (int bill : bills) {
      collected[bill]++;

      if (bill == price) {
        continue;
      }

      int change = bill - price;
      for (int note : {10, 5}) {
        if (change / note > 0 && collected[note] > 0) {
          int numNotes = std::min(change / note, collected[note]);
          collected[note] -= numNotes;
          change -= note * numNotes;
        }
      }

      if (change) {
        return false;
      }
    }

    return true;
  }
};