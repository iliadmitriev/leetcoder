
import string


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        """Returns the minimum number of characters to add,
        delete or insert to make the password.

        Args:
            password: input string of characters.

        Returns:
            minimum number of characters to add, delete or insert.
        """
        upper = set(string.ascii_uppercase)
        lower = set(string.ascii_lowercase)
        digits = set(string.digits)

        deletions = max(0, len(password) - 20)
        has_upper = any(c in upper for c in password)
        has_lower = any(c in lower for c in password)
        has_digit = any(c in digits for c in password)

        missing_types = int(not has_upper) + int(not has_lower) + int(not has_digit)

        substring_lengths = self.count_substring(password)

        self.break_str_with_deletion(substring_lengths, deletions)
        num_substring_breaks = sum(
            length // 3 for length in substring_lengths if length >= 3
        )

        insertions = max(0, 6 - len(password))

        return deletions + max(num_substring_breaks, missing_types, insertions)

    def count_substring(self, password: str) -> list[int]:
        """Returns list of number of times each character repeats.

        abcdddaaa -> [1, 2, 1, 4]

        Args:
            password: input string of characters

        Returns:
            list of length of each repeated character
        """
        res: list[int] = []
        prev = None
        for cur in password:
            if not res or cur != prev:
                res.append(1)
            else:
                res[-1] += 1

            prev = cur

        return res

    def break_str_with_deletion(self, substring_lengths: list[int], deletions: int):
        """Deletes from substring_lengths as much as deletions.

        Args:
            substring_lengths: count of times each character repeats
            deletions: numnber of times to delete
        """
        while deletions > 0:
            delete_idx, *_ = min(
                enumerate(substring_lengths),
                key=lambda x: x[1] % 3 if x[1] >= 3 else float("inf"),
            )
            substring_lengths[delete_idx] -= 1
            deletions -= 1

