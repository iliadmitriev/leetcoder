func totalMoney(n int) int {
    week, rest := n / 7, n % 7

    // formula sum of arithmetic progression
    // S = count * (first + last) / 2

    // 0: 1 + .. + 7 = 28
    // 1: 2 + .. + 8 = 35 (+7)
    // 2: 3 + .. + 9 = 42 (+7)
    // ...
    // w: w+1 + .. + w+r = 28 + (w - 1) * 7

    // whole weeks progression sum (start from 28, +7 increment)
    // first = 28
    // last = 28 + (w - 1) * 7
    // count = w
    res := week * (28 + 28 + (week - 1) * 7) / 2

    // rest of the week days progression (on the week w)
    // first = w + 1
    // last = w + r
    // count = r
    res += rest * (week + 1 + week + rest) / 2

    return res
}