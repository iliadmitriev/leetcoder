class Solution {
public:
  int maxBottlesDrunk(int numBottles, int numExchange) {
        int empty = numBottles;
        

            while (empty >= numExchange) {
                empty -= numExchange;
                empty++;
                numBottles++;
                numExchange++;
            }

        return numBottles;
    }
};
