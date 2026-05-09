import "math/big"

func countGoodNumbers(n int64) int {
	mod := big.NewInt(1e9 + 7)
	odd, even := big.NewInt(n-n/2), big.NewInt(n/2)
	base5, base4 := big.NewInt(5), big.NewInt(4)

	odd.Exp(base5, odd, mod)
	even.Exp(base4, even, mod)

	odd.Mul(odd, even).Mod(odd, mod)

	return int(odd.Int64())
}
