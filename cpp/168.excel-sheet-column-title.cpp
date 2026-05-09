class Solution {
public:
    string convertToTitle(int columnNumber) {
        string res;
        while (columnNumber) {
            columnNumber--;
            char rem = 'A' + columnNumber % 26;
            res += rem;
            columnNumber /= 26;
        };
        reverse(res.begin(), res.end());
        return res;
    }
};