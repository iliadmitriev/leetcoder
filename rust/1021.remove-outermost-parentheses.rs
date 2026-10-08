impl Solution {
    pub fn remove_outer_parentheses(s: String) -> String {
        let mut res: Vec<char> = vec![];
        let mut depth = 0;
        
        for ch in s.chars() {
            if ch == '(' && depth > 0 {
                res.push(ch);
            } else if ch == ')' && depth > 1 {
                res.push(ch);
            }
            
            depth += match (ch) {
                '(' => 1,
                ')' => -1,
                _ => unreachable!(),
            }
        }
        
        res.iter().collect()
    }
}