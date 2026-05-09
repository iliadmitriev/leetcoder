func myPow(x float64, n int) float64 {
    if n == 0 {
        return 1.0
    } else if n < 0 {
        return 1.0 / myPow(x, -n)
    } else if n % 2 == 1 {
        return x * myPow(x * x, n / 2)
    } else {
        return myPow(x * x, n / 2)
    }   
}