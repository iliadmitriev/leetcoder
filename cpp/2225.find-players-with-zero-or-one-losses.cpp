class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        map<int, int> scores;

        for (const auto& match: matches) {
            if (scores.find(match[0]) == scores.end()) {
                scores[match[0]] = 0;
            }

            scores[match[1]]++;
        }

        vector<int> zero, one;

        for (auto [player, count]: scores) {
            switch (count) {
                case 0: zero.push_back(player); break;
                case 1: one.push_back(player); break;
            }
        }

        return { zero, one };
    }
};