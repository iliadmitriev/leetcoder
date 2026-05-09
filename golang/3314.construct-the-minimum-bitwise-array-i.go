/*
x | (x + 1) = n

x = 10100011
    10100100
n = 10100111 - 167
        *
    00001000
for earch n:
1) get LSB == 0 from n (3)
2) shift right
3) xor

n:
    10100111
n + 1:
    10101000
^n:
    01011000
&:
    00001000
>>:
    00000100
^:
    10100011

*/
func minBitwiseArray(nums []int) []int {
    res := make([]int, len(nums))

    for i, n := range nums {
      if n & 1 != 1 {
        res[i] = -1
        continue
      }

      bit := (n + 1) & (^n)
      bit >>= 1

      res[i] = n ^ bit
    }

    return res
}