type Key struct{
    mask int
    op int
}

type Cache map[Key]int

var cache Cache

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func gcd(x, y int) int {
    for y > 0 {
        x, y = y, x % y
    }
    return x
}

func dp(nums []int, mask int, op int) int {
    if op > len(nums) / 2 {
        return 0
    }

    if value, ok := cache[Key{mask, op}]; ok {
        return value
    }

    res := 0

    for i := 0; i < len(nums); i++ {
        for j := i + 1; j < len(nums); j++ {
            if mask & (1 << i) | mask & (1 << j) > 0 {
                continue
            }

            new_mask := mask | (1 << i) | (1 << j)
            res = max(
                res,
                op * gcd(nums[i], nums[j]) + dp(nums, new_mask, op + 1),
            )
        }
    }

    cache[Key{mask, op}] = res
    return res
}

func maxScore(nums []int) int {
    cache = make(Cache)

    return dp(nums, 0, 1)
}