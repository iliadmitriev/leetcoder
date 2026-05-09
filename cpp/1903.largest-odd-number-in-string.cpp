class Solution {
public:
    string largestOddNumber(string num) {
        int j = 0;
        for (int i = 0; i < num.size(); i++) {
            if (num[i] & 1) {
                j = i + 1;
            }
        }
        return num.substr(0, j);
    }
};