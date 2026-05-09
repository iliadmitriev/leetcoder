const MOD int = 1337

func pow(base int, exp int) int {
    base %= MOD
    if base == 1 {
        return 1
    }

    result := 1
    for exp > 0 {
        if exp % 2 == 1 {
            result = (result * base) % MOD
        }
        exp /= 2
        base = (base * base) % MOD
    }
    return result
}

func superPow(a int, b []int) int {
    out := 1
    for _, exp := range b {
        out = pow(out, 10) * pow(a, exp) % MOD
    }
    return out
}