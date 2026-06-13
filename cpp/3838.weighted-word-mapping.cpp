class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        auto worder = [&weights](string& word) -> char {
            int s = 0;

            for (char ch : word) {
                s += weights[ch - 'a'];
            }

            return 'z' - (s % 26);
        };

        auto res = words | std::views::transform(worder);

        return string(res.begin(), res.end());
    }
};