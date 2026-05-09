

class Solution:
    def validateCoupons(
        self, code: list[str], businessLine: list[str], isActive: list[bool]
    ) -> list[str]:
        validBusinessLines = {"electronics", "grocery", "pharmacy", "restaurant"}

        data = sorted(
            filter(
                lambda x: len(x[1]) > 0
                and all(c.isalnum() or c == "_" for c in x[1])
                and x[0] in validBusinessLines
                and x[2],
                zip(businessLine, code, isActive),
            ),
        )

        return [code for _, code, _ in data]

