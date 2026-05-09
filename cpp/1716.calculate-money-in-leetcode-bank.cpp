class Solution {
public:
    int totalMoney(int n) {
        int week = n / 7;
        int rest = n % 7;

        int res = 0;

        // arithmetic sum formula
        // s = count * (first + last) / 2

        // 1 + .. + 7 = 28
        // 2 + .. + 8 = 35 (+7)
        // 3 + .. + 9 = 42 (+7)
        //     ..
        // w+1 .. w+r = 28 + (w-1) * 7

        // whole weeks
        // first = 28
        // last = 28 + (w - 1) * 7
        // count = w
        res += week * (28 + 28 + (week - 1) * 7) / 2;

        // last days of the rest of the week
        // first = w + 1
        // last = w + r
        // count = r
        res += rest * (week + 1 + week + rest) / 2;

        return res;
    }
};