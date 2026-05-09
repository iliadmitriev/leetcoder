func minPartitions(n string) int {
   x := 0
   base := rune('0')

   for _, v := range n {
    x = max(x, int(v - base))
   }

   return x 
}