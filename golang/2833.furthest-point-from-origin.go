func furthestDistanceFromOrigin(moves string) int {
  pos := 0
  spc := 0

  abs := func(x int) int {
    if x < 0 {
      return -x
    }

    return x
  }

  for _, m := range moves {
    switch m {
      case 'R': pos++
      case 'L': pos--
      case '_': spc++
    }
  }
    
  return abs(pos) + spc
}