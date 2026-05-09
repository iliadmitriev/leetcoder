class Solution:
    def intToRoman(self, num: int) -> str:
        hundred = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        unit = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return ("M" * (num // 1000) + hundred[(num % 1000) // 100] +
                ten[(num % 100) // 10] + unit[num % 10])
