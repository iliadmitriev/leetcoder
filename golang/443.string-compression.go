import (
	"strconv"
)

func compress(chars []byte) int {
	cur := 1
	j := 0

	write := func(b byte) int {
		chars[j] = b
        j++

		if cur > 1 {
			num := strconv.Itoa(cur)
			for k := range num {
				chars[j] = num[k]
				j++
			}
		}

        return j
	}

	for i := 1; i < len(chars); i++ {
		if chars[i-1] == chars[i] {
			cur++
		} else {
			write(chars[i-1])
			cur = 1
		}
	}

	write(chars[len(chars)-1])

	return j
}