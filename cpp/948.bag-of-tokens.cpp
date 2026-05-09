class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int left = 0, right = tokens.size() - 1;
        int score = 0;

        std::sort(tokens.begin(), tokens.end());

        while (left <= right) {
            if (power >= tokens[left]) {
                power -= tokens[left++];
                score++;
            } else if (left + 1 < right && score) {
                power += tokens[right--];
                score--;
            } else {
                break;
            }
        }

        return score;
    }
};