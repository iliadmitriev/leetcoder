import collections


class Solution:
    def reformat(self, s: str) -> str:
        digits, letters = collections.deque(), collections.deque()

        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else:
                letters.append(ch)

        n_digits, n_letters = len(digits), len(letters)

        if n_digits < n_letters:
            digits, letters = letters, digits
            n_digits, n_letters = n_letters, n_digits

        if n_digits - n_letters > 1:
            return ""

        res = []
        for i in range(n_letters):
            res.append(digits.popleft())
            res.append(letters.popleft())

        if digits:
            res.append(digits.popleft())

        return "".join(res)

