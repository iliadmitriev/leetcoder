func minNumberOfSeconds(mountainHeight int, workerTimes []int) int64 {

  const eps = 1e-7

  maxWorker := workerTimes[0]
  for _, v := range workerTimes {
    maxWorker = max(maxWorker, v)
  }

  lo, hi := 0, mountainHeight * (mountainHeight + 1) * maxWorker
  ans := int64(0)

  for lo <= hi {

    mid := (lo + hi) / 2

    cnt := 0
    for _, w := range workerTimes {
      t := mid / w
      cnt += int((-1.0 + math.Sqrt(1 + float64(t) * 8)) / 2 + eps)
    }

    if cnt >= mountainHeight { // fit
      ans = int64(mid)
      hi = mid - 1
    } else {
      lo = mid + 1
    }
  }
    
  return ans
}