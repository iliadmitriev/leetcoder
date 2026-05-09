import (
    "math"
)

func buyChoco(prices []int, money int) int {
    min1, min2 := math.MaxInt, math.MaxInt
    for _, price := range prices {
        if min1 > price {
            min1, min2 = price, min1
        } else if min2 > price {
            min2 = price
        }
    }

    if min1 + min2 <= money {
        return money - (min1 + min2)
    }
    return money
}