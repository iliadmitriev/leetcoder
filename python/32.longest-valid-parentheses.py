class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def scan(seq, opening_symb="(") -> int:
            res = 0
            opening, closing = 0, 0
            for item in seq:
                if item == opening_symb:
                    opening += 1
                else:
                    closing += 1

                if opening == closing:
                    res = max(opening + closing, res)

                if opening < closing:
                    opening, closing = 0, 0

            return res

        return max(
            scan(s, "("),
            scan(reversed(s), ")"),
        )
