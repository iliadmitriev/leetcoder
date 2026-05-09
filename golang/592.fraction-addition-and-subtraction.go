
type Fraction struct {
	Num, Den int
}

func ParseFrac(s string) Fraction {
	del := strings.IndexByte(s, '/')
	num, _ := strconv.Atoi(s[:del])
	den, _ := strconv.Atoi(s[del+1:])

	return Fraction{num, den}
}

func (f *Fraction) Reduce() {
	n := f.Num
	if n < 0 {
		n = -n
	}

	g := __gcd(n, f.Den)
	f.Num /= g
	f.Den /= g
}

func (f *Fraction) Add(g Fraction) {
	f.Num = f.Num*g.Den + f.Den*g.Num
	f.Den *= g.Den
}

func __gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func fractionAddition(expression string) string {
	res := ParseFrac("0/1")

	for i, j := 0, 1; j <= len(expression); j++ {
		if j == len(expression) || expression[j] == '+' || expression[j] == '-' {

			res.Add(ParseFrac(expression[i:j]))

			i = j
		}
	}

	res.Reduce()

	return fmt.Sprintf("%d/%d", res.Num, res.Den)
}
