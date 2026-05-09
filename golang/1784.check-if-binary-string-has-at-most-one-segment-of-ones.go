func checkOnesSegment(s string) bool {
   cur := 0
   cnt := 0

   for _, ch := range s {
    d := int(ch - '0')

    if d == 1 {
      cur++
    } else {
      if cur > 0 {
        cnt++
      }
      cur = 0
    }
   }

   if cur > 0 {
    cnt++
   }

   return cnt <= 1
}