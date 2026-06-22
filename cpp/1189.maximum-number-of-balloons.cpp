class Solution {
public:
    int maxNumberOfBalloons(string text) {
        vector<int> symbols(26);
        char a = 'a';

        for (char c : text) {
            symbols[c - a]++;
        }

        int res = text.size();
        res = std::min(res, symbols['b' - a]);
        res = std::min(res, symbols['a' - a]);
        res = std::min(res, symbols['l' - a] / 2);
        res = std::min(res, symbols['o' - a] / 2);
        res = std::min(res, symbols['n' - a]);

        return res;
    }
};