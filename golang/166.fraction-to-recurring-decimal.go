import (
	"fmt"
	"strconv"
	"strings"
)

func fractionToDecimal(numerator int, denominator int) string {
	if numerator == 0 {
		return "0"
	}

	res := strings.Builder{}

	if (numerator < 0) != (denominator < 0) {
		res.WriteByte('-')
	}

	if numerator < 0 {
		numerator = -numerator
	}

	if denominator < 0 {
		denominator = -denominator
	}

	res.WriteString(strconv.Itoa(numerator / denominator))
	numerator %= denominator
	numerator *= 10

	if numerator == 0 {
		return res.String()
	}

	res.WriteByte('.')
	cache := make(map[int]int)

	for numerator != 0 && cache[numerator] == 0 {
		cache[numerator] = res.Len()
		res.WriteString(strconv.Itoa(numerator / denominator))
		numerator %= denominator
		numerator *= 10
	}

	final := res.String()

	if numerator != 0 {
		i := cache[numerator]
		final = fmt.Sprintf("%s(%s)", final[:i], final[i:])
	}

	return final
}
