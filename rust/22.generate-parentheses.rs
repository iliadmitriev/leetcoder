impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut res = Vec::new();

        fn dfs(opening: i32, closing: i32, s: String, res: &mut Vec<String>) {
            if opening > closing {
                return;
            }

            if opening == 0 && closing == 0 {
                res.push(s);
                return;
            }

            if opening > 0 {
                dfs(opening - 1, closing, format!("{}(", s), res);
            }

            if closing > 0 {
                dfs(opening, closing - 1, format!("{})", s), res);
            }
        }

        dfs(n, n, String::new(), &mut res);

        res
    }
}
