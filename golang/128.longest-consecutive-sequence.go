/*

           *
[100,4,200,1,3,2]

*/
func longestConsecutive(nums []int) int {
  numset := make(map[int]bool, len(nums)) 
  for _, num := range nums { numset[num] = true }

  seq := 0

  for num := range numset {
    // if it't not a start
    if _, ok := numset[num - 1]; ok {
      continue
    }

    cnt := 0
    for numset[num + cnt] {
      cnt++
    }

    seq = max(seq, cnt)
  }

  return seq
}