func destCity(paths [][]string) string {
  outorder := map[string]bool{}

  for _, path := range paths {
    outorder[path[0]] = true
  }

  for _, path := range paths {
    if !outorder[path[1]] {
      return path[1]
    }
  }
    
  return "" 
}