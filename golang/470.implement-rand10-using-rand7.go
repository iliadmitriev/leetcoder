// var rand7 func() int
// | [1;7] x [1;7] | = 49
func rand10() int {
	for {

		r := ((rand7()-1)*7 + rand7() - 1)
		if r < 40 {
			return r%10 + 1
		}
	}
}