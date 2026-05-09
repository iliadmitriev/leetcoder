
func z(a int) int {
    if a < 0 {
        return 0
    }
    return a
}


func dpWithCache() func(int, int) float64 {
    cache := make(map[int]map[int]float64)

    var dp func (i int, j int) float64

    dp = func (i int, j int) float64 {
        // check cache
        if value, ok := cache[i]; ok {
            if value2, ok2 := value[j]; ok2 {
                return value2
            }
        } else {
            cache[i] = map[int]float64{}
        }

        var res float64
        if i == 0 && j == 0 {
            res = 0.5
        } else if i == 0 {
            res = 1.0
        } else if j == 0 {
            res = 0.0
        } else {
            res = ( dp(z(i - 100), j) + dp(z(i - 75), z(j - 25)) + dp(z(i - 50), z(j - 50)) + dp(z(i - 25), z(j - 75)) ) / 4.0
        }

        cache[i][j] = res
        return res

    }

    return dp

}

func soupServings(n int) float64 {
    if n >= 4500 {
        return 1.0
    }

    dp := dpWithCache()

    return dp(n, n)
    
}