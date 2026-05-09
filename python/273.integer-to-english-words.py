class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        def helper(num: int) -> list[str]:
            if num == 0:
                return []

            v: list[str] = []

            if num < 20:
                v.append(digits[num])
            elif num < 100:
                v.append(tens[num // 10])
                v.extend(helper(num % 10))
            elif num < 1000:
                v.extend(helper(num // 100))
                v.append("Hundred")
                v.extend(helper(num % 100))
            elif num < 1000000:
                v.extend(helper(num // 1000))
                v.append("Thousand")
                v.extend(helper(num % 1000))
            elif num < 1000000000:
                v.extend(helper(num // 1000000))
                v.append("Million")
                v.extend(helper(num % 1000000))
            else:
                v.extend(helper(num // 1000000000))
                v.append("Billion")
                v.extend(helper(num % 1000000000))

            return v

        digits = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        v = helper(num)
        return " ".join(v)

