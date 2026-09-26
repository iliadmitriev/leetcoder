use std::collections::HashMap;

impl Solution {
    pub fn evaluate(s: String, knowledge: Vec<Vec<String>>) -> String {
        let voc: HashMap<String, String> = knowledge
            .into_iter()
            .map(|inner| {
                let [key, val]: [String; 2] = inner.try_into().expect("knowledge vector must have exactly 2 elements");
                (key, val)
            })
            .collect();

        let mut i = 0;

        let mut res = String::with_capacity(s.len());
        let mut cur_key = String::new(); // current key collector
        let mut par = false; // in parentheses

        for c in s.chars() {
            match c {
                '(' => {
                    par = true;
                }
                ')' => {
                    par = false;

                    match voc.get(&cur_key) {
                        Some(val) => res.push_str(val),
                        None => res.push('?'),
                    }

                    cur_key.clear();
                }
                _ => {
                    match par {
                      true => cur_key.push(c),
                      false => res.push(c),
                    }
                }
            }
        }

        res
    }
}
