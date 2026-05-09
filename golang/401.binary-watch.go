import (
  "math/bits"
  "fmt"
)

func readBinaryWatch(turnedOn int) []string {
  res := make([]string, 0)

  for h := range uint(12) {
    for m := range uint(60) {
      if bits.OnesCount(h) + bits.OnesCount(m) == turnedOn {
        res = append(res, fmt.Sprintf("%d:%02d", h, m))
      }
    }
  }

  return res
}