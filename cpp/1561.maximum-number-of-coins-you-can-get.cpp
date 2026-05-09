class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int top = 0;
        map<int, int> mp;
        for (auto x : piles) {
            mp[x]++;
            if (x > top) {
                top = x;
            }
        }
        int res = 0;
        for (int n = piles.size() / 3; n > 0; n--) {
            // get next top values from the pile and remove it
            while (top > 0 && mp[top] == 0) {
                top--;
            }
            mp[top]--;

            // get next top values from the pile and remove it
            while (top > 0 && mp[top] == 0) {
                top--;
            }
            mp[top]--;

            res += top;
        }
        return res;
    }
};