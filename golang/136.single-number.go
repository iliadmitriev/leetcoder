func singleNumber(nums []int) int {
   xx := 0

   for _, x := range nums {
    xx ^= x
   }

   return xx
}