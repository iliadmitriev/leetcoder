const MOD = int(1e9) + 7

func countHomogenous(s string) int {
    total := 0
    var i, j int
    for i = 0; i < len(s); {
        for j = i + 1; j < len(s) && s[i] == s[j]; j++ {}
        total += (j - i) * (j - i + 1) / 2
        i = j
    }

    return total % MOD
}