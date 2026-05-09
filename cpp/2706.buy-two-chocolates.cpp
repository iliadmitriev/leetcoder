class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int min1 = numeric_limits<int>::max();
        int min2 = numeric_limits<int>::max();

        for (auto price: prices) {
            if (min1 > price) {
                min2 = min1; min1 = price;
            } else if (min2 > price) {
                min2 = price;
            }
        }

        if (min1 + min2 <= money) {
            return money - (min1 + min2);
        }
        return money;
    }
};