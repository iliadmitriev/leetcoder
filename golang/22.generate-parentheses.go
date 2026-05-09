// 3 options:
// A: wrap (%s)
// B: concatenate left %s()
// C: concatenate right ()%s
// base: n == 0 ""
// n = 1 "()"
// n = 2 "(())", "()()" 
// n = 3 "((()))", "(())()", "(()())", "()()()", !"()(())"
// n = 4 "(((())))", "((()))()", "((())())", "(())()()", "((()()))", "(()())()", "(()()())", "()()()()", !"(()(()))", ...
func generateParenthesis(n int) []string {
    var dfs func(int) []string
    dfs = func(n int) []string {
      if n == 0 {
        return []string{""}
      }

      res := make([]string, 0)
      for i := range n {
        for _, left := range dfs(i) { // "" | (), "" 
          for _, right := range dfs(n - i - 1) { // "()", "" | ""
            res = append(res, fmt.Sprintf("%s(%s)", left, right))
          }
        }
      }

      return res
    }

    return dfs(n)
}