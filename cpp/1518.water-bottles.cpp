class Solution {
public:
  int numWaterBottles(int numBottles, int numExchange) {
    int empty = 0, total = 0;

    while (numBottles) {
      total += numBottles;
      empty += numBottles;
      numBottles = empty / numExchange;
      empty %= numExchange;
    }

    return total;
  }
};