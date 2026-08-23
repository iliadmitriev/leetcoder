func sumGame(num string) bool {
    collect := func(l, r int) (n, q int) {
      for k := l; k < r; k++ {
        if num[k] == '?' {
          q++
        } else {
          n += int(num[k] - '0')
        }
      }

      return n, q
    }

    n := len(num)
    n0, q0 := collect(0, n / 2)
    n1, q1 := collect(n / 2, n)
    
    return (q0 + q1) % 2 == 1 || n0 - n1 != (q1 - q0) * 9 / 2
}