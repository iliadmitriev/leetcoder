func separateSquares(squares [][]int) float64 {
	const Eps = 1e-6

	n := len(squares)
	sq := make([][3]float64, 0, n)
	lo := math.Inf(1)
  hi := math.Inf(-1)
  
  var mid float64

	for _, s := range squares {
    bottom := float64(s[1])
    size := float64(s[2])
    top := bottom + size
    sq = append(sq, [3]float64{bottom, top, size})

    lo = min(lo, bottom)
    hi = max(hi, top)
	}

  isBottomGreater := func(mid float64) bool {
    var bottom, top float64

    for _, s := range sq {
      if s[0] >= mid {
        top += s[2] * s[2]
      } else if s[1] <= mid {
        bottom += s[2] * s[2]
      } else {
        top += (s[1] - mid) * s[2]
        bottom += (mid - s[0]) * s[2]
      }
    }

    return bottom >= top
  }

  for hi - lo > Eps {
    mid = lo + (hi - lo) / 2

    if isBottomGreater(mid) {
      hi = mid
    } else {
      lo = mid
    }

  }

  return lo
}