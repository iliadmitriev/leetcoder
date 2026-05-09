#include <stack>
#include <vector>

using std::vector, std::stack;

class Solution {
public:
  vector<int> finalPrices(vector<int> &prices) {
    const int n = prices.size();

    vector<int> pricesWithDiscount(prices);
    stack<int> st;

    for (int i = 0; i < n; i++) {
      while (!st.empty() && pricesWithDiscount[st.top()] >= prices[i]) {
        pricesWithDiscount[st.top()] -= prices[i];
        st.pop();
      }

      st.push(i);
    }

    return pricesWithDiscount;
  }
};