import (
    "sort"
)

const MOD = int(1e9) + 7;

func numFactoredBinaryTrees(arr []int) int {
    sort.Ints(arr)
    res := 0
    dp := make(map[int]int)
    for i := 0; i < len(arr); i++ {
        dp[arr[i]] = 1
    }

    for i := 0; i < len(arr); i++ {
        for j := 0; j < len(arr); j++ {
            a := arr[i] / arr[j]
            b := arr[i] % arr[j]

            if a == 0 {
                break
            }

            if v, ok := dp[a]; b == 0 && ok {
                dp[arr[i]] += v * dp[arr[j]]
                dp[arr[i]] %= MOD
            }
        }
    }

    for _, v := range dp {
        res += v
        res %= MOD
    }

    return res
}