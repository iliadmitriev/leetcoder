/*
In a subtring :
a -b , b-c
a -b , c
a - c , b
b - c , a
must be same at staring and end points .

A substring can contain longest substring having only single character like in this:

bacaaaaaaaaaaaaabacbabcbabcb

iterative pass for longest substring with single character using 2 pointers for this

*/
func longestBalanced(s string) int {
	type key = [2]int32

	longestSingle := func(s string) int {
		a, b, c, ma := 0, 0, 0, 0
		for i := range len(s) {
			switch s[i] {
			case 'a':
				a, b, c, ma = a+1, 0, 0, max(ma, b, c)

			case 'b':
				a, b, c, ma = 0, b+1, 0, max(ma, a, c)

			default:
				a, b, c, ma = 0, 0, c+1, max(ma, a, b)
			}
		}

		return max(ma, a, b, c)
	}

	recalc := func(result, i int, m map[key]int32, k key) int {
		j, has := m[k]
		if has {
			return max(result, i-int(j))
		}
		m[k] = int32(i)

		return result
	}

	longestAbc := func(s string) int {
		m := [4]map[key]int32{
			map[key]int32{key{}: -1},
			map[key]int32{key{}: -1},
			map[key]int32{key{}: -1},
			map[key]int32{key{}: -1},
		}

		abc := [3]int32{}
		result := 0

		for i := range len(s) {
			abc[s[i]-'a']++
			result = recalc(result, i, m[0], key{abc[0] - abc[1], abc[0] - abc[2]})
			result = recalc(result, i, m[1], key{abc[0] - abc[1], abc[2]})
			result = recalc(result, i, m[2], key{abc[1] - abc[2], abc[0]})
			result = recalc(result, i, m[3], key{abc[2] - abc[0], abc[1]})
		}

		return result
	}

	return max(longestSingle(s), longestAbc(s))
}