class Solution {
public:
    string largestGoodInteger(string num) {
        int cur = 0, n = 0;

        for (int i = 0; i < num.size() - 2; i++) {
            if (num[i] == num[i + 1] && num[i] == num[i + 2]) {
                if (n == 0 || num[i] >= num[cur]) {
                    n = 3;
                    cur = i;
                }
            }
        }

        return num.substr(cur, n);
    }
};