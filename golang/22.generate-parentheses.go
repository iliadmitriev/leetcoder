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
    res := make([]string, 0)

    var dfs func(int, int, string)

    dfs = func(opening, closing int, s string) {
      if opening == 0 && closing == 0 {
        res = append(res, s)
        return
      }

      // condition is inverted 'cause it's how much left (and not how much used)
      if opening > closing { 
        return
      }

      if opening > 0 {
        dfs(opening - 1, closing, s + "(")
      }

      if closing > 0  {
        dfs(opening, closing - 1, s + ")")
      }
    }

    dfs(n, n, "")

    return res
}