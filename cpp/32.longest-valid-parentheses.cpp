class Solution {
public:
    int longestValidParentheses(string s) {
        auto scan = [](auto start, auto end, char op) -> int {
            int res = 0, opening = 0, closing = 0;

            for (auto it = start; it != end; it++) {
                if (*it == op) {
                    opening++;
                } else {
                    closing++;
                }

                if (opening == closing) {
                    res = std::max(res, opening + closing);
                }

                if (opening < closing) {
                    closing = 0;
                    opening = 0;
                }
            }

            return res;
        };

        return std::max(scan(s.begin(), s.end(), '('),
                        scan(s.rbegin(), s.rend(), ')'));
    }
};