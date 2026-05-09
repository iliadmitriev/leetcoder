class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int cnt1 = count_if(s.begin(), s.end(), [](auto c) -> bool { return c == '1'; });
        int cnt0 = s.size() - cnt1;

        stringstream ss;

        while (cnt1 > 1) {
            ss << "1";
            cnt1--;
        }

        while (cnt0) {
            ss << "0";
            cnt0--;
        }

        ss << "1";
        return ss.str();
    }
};