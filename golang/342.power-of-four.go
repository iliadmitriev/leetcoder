func isPowerOfFour(n int) bool {
    oddMask := 0x55555555
    return n > 0 && n & (n - 1) == 0 && oddMask & n == n
}