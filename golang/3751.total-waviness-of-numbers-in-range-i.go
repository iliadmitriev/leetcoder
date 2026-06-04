func totalWaviness(num1 int, num2 int) int {
    count := func(x int) int {
      if x < 101 {
        return 0
      }

      var c, r2, r1, r int

      r2 = x % 10
      x /= 10
      r1 = x % 10
      x /= 10

      for ; x > 0; x /= 10 {
        r = x % 10

        if (r2 < r1 && r1 > r) || (r2 > r1 && r1 < r) {
          c++
        }

        r2, r1 = r1, r
      }

      return c
    }


    res := 0
    for x := num1; x <= num2; x++ {
      res += count(x)
    }

    return res
}