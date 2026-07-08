const (
	MOD    = int64(1e9 + 7)
	MAX_SZ = int(1e5 + 1)
)

var POW10 []int64

func init() {
	POW10 = make([]int64, MAX_SZ)
	POW10[0] = 1

	for i := 1; i < MAX_SZ; i++ {
		POW10[i] = POW10[i-1] * 10 % MOD
	}
}

func sumAndMultiply(s string, queries [][]int) []int {
	n := len(s)
	m := len(queries)

	sum := make([]int, n+1)
	x := make([]int64, n+1)
	cnt := make([]int, n+1)
	res := make([]int, m)

	for i := 0; i < n; i++ {
		d := int(s[i] - '0')

		sum[i+1] = sum[i] + d

		if d > 0 {
			cnt[i+1] = cnt[i] + 1
			x[i+1] = (x[i]*10 + int64(d)) % MOD
		} else {
			cnt[i+1] = cnt[i]
			x[i+1] = x[i]
		}
	}

	for j, q := range queries {
		l, r := q[0], q[1]+1 // not inclusive

		length := cnt[r] - cnt[l] // real length skipping 0's

		val_x := (MOD + x[r] - x[l]*POW10[length]%MOD) % MOD
		val_s := int64(sum[r] - sum[l])

		res[j] = int((val_x * val_s) % MOD)
	}

	return res
}